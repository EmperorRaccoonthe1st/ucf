function cd_removeCourseDesignationsStorage(key) {
  try {
    localStorage.removeItem(key);
    localStorage.removeItem(key + "_expiresIn");
  } catch (e) {
    console.log(
      `Course Designations: removeCourseDesignationsStorage: ` +
      `Error removing key [${key}] from localStorage: `, e
    );
    return false;
  }
  return true;
}

function cd_getCourseDesignationsStorage(key) {
  var now = Date.now(); //epoch time, lets deal only with integer
  // set expiration for storage
  var expiresIn = localStorage.getItem(key + "_expiresIn");
  if (expiresIn === undefined || expiresIn === null) {
    expiresIn = 0;
  }

  if (expiresIn < now) {
    // Expired
    cd_removeCourseDesignationsStorage(key);
    return null;
  } else {
    try {
      var value = localStorage.getItem(key);
      return value;
    } catch (e) {
      console.log(`Course Designations: Error reading localStorage key ${key}`, e);
      return null;
    }
  }
}

function cd_setCourseDesignationsStorage(key, value, expires) {
  if (expires === undefined || expires === null) {
    expires = 24 * 60 * 60; // default: seconds for 6 hours (6*60*60)
  } else {
    expires = Math.abs(expires); //make sure it's positive
  }

  var now = Date.now(); //millisecs since epoch time, lets deal only with integer
  var schedule = now + expires * 1000;
  try {
    localStorage.setItem(key, value);
    localStorage.setItem(key + "_expiresIn", schedule);
  } catch (e) {
    console.log(
      `Course Designations: setStorage: Error settings key [${key}] in localStorage: `, e
    );
    return false;
  }
  return true;
}

// ===========================================================================

// Enumerated values for options in the Course Designations LTI App
const course_designations_screens = {
  FRONTPAGE: "Front Page",
  MODULES: "Modules",
  ASSIGNMENTS: "Assignments",
  SYLLABUS: "Syllabus",
  ANNOUNCEMENTS: "Announcements"
}

const course_designations_locations = {
  TOPOFPAGE: "Top of Page",
  ALONGSIDEHEADER: "Alongside Header",
  BOTTOMOFPAGE: "Bottom of Page",
  CUSTOMINSERTION: "Custom Location"
}

const course_designations_spacings = {
  LEFT: "Left",
  CENTER: "Center",
  RIGHT: "Right",
  SPREAD: "Spread Out",
}

function cd_isOnCourseDesignationsScreen(courseData, courseId) {
  let path = "/courses/" + courseId;
  let pageSpecificElement = '';
  switch (courseData.display_page) {
    case course_designations_screens.MODULES:
      path += "/modules";
      pageSpecificElement = "#context_modules_sortable_container";
      break;
    case course_designations_screens.ASSIGNMENTS:
      path += "/assignments";
      pageSpecificElement = "#ag-list";
      break;
    case course_designations_screens.SYLLABUS:
      path += "/external_tools/374802";   // Simple Syllabus.
      pageSpecificElement = "#course_syllabus";  // THIS is a backup for the "Syllabus" page, which should not be used.
      break;
    case course_designations_screens.ANNOUNCEMENTS:
      path += "/announcements";
      pageSpecificElement = ".announcements-v2__wrapper";
      break;
    default:
      break;
  }

  /*******************************************************************************************
   * If the path matches OR the page-specific element is found, we're on the right screen.
   * The element check is necessary when designations are set to a specific page (like the
   * modules page), and that page is set as the front page of the course. In that case, the
   * path will not match when we're on the front page, but we still want the designation to
   * show there because it is still the modules page.
   * 
   * Note that the pageSpecificElement check is REALLY, REALLY brittle, and if Canvas changes
   * the id or class names of the elements we're looking for, it will break.
   ******************************************************************************************/
  if(window.location.pathname === path) {
    return true;
  }
  if (pageSpecificElement && document.querySelector(pageSpecificElement)) {
    return true;
  }
  if (courseData.display_location === course_designations_locations.CUSTOMINSERTION) {
    if (document.getElementById("course-designations-location")) {
      return true;
    }
  }

  return false;
}

// This function places correct designations in the correct location in the correct screen with the correct size
function cd_placeCourseDesignations(courseData, courseId) {

  if(!cd_isOnCourseDesignationsScreen(courseData, courseId)) {
    return;
  }
  
  let isFaculty = cd_isFacultyView();
  // Create the HTML for all of the Course Designation images.
  let imgTags = "";
  for (let designation of courseData.designations_displayed) {
    let tempTitle = courseData.designation_info[designation.id].fullName +
                    ' Course Designation' +
                    (isFaculty ? ' - Click to edit' : '');
    imgTags += `<img width=${courseData.size} ` +
      `height=${courseData.size} ` +
      `src=${courseData.designation_info[designation.id].imageUrl} ` +
      `title="${tempTitle}" ` +
      `aria-label="${tempTitle}" ` +
      `aria-description="${courseData.designation_info[designation.id].description}" />`;
  }

  let mainContent = document.querySelector("div[role='main']");
  let header = mainContent.querySelector("h1:not(.screenreader-only)");

  // Create the image container div with the appropriate spacing. Default justification is CENTER.
  let commonStyle = "display:flex;flex-wrap:wrap;width:100%;box-sizing:border-box;align-items:center;";
  let justificationStyle = "gap:2em;padding:1em 2em;justify-content:center;";
  if (courseData.spacing === course_designations_spacings.LEFT) {
    justificationStyle = "gap:2em;padding:1em 2em 1em 0;justify-content:flex-start;";
  } else if (courseData.spacing === course_designations_spacings.RIGHT) {
    justificationStyle = "gap:2em;padding:1em 0 1em 2em;justify-content:flex-end;";
  } else if (courseData.spacing === course_designations_spacings.SPREAD) {
    justificationStyle = "gap:2em;padding:1em 2em;justify-content:space-evenly;";
  }
  // If "Alongside Header" is selected and there IS a header, we want this right-aligned with no padding.
  if (courseData.display_location === course_designations_locations.ALONGSIDEHEADER && header) {
    justificationStyle = "gap:1em;padding:0;justify-content:flex-end;";
  }
  let courseDesignationContainer = `<div style="${commonStyle + justificationStyle}">${imgTags}</div>`;

  if (isFaculty) {
    courseDesignationContainer = `<a ` +
      `href="/courses/${courseId}/external_tools/412747" ` +
      `target="_blank" ` +
      `rel="noopener noreferrer" ` +
      `title="Click to edit Course Designations" ` +
      `aria-label="Course Designations Settings Page">` +
      `${courseDesignationContainer}</a>`;
  }

  /************************************************************************************************
   * In Canvas, the main page content is inside a dive with the role of "main".
   * 
   * <div id="content-wrapper" class="ic-Layout-contentWrapper">  (padding and centering)
   *   <div id="content" class="ic-Layout-contentMain" role="main"> (main content of the page)
   * 
   * We want the Course Designations to either be the first thing in the main content, the last
   * thing in the main content, or alongside the header of the main content. If the header cannot
   * be found, we will default to the top of the main content.
   * 
   * The same logic applies to the "custom insertion" option, except instead of looking for the
   * header, we will look for an element with the id of "course-designations-location". If that
   * element cannot be found, we will default to the top of the main content.
   ***********************************************************************************************/

  let customLocation = document.getElementById("course-designations-location");
  
  if (courseData.display_location === course_designations_locations.CUSTOMINSERTION) {
    if (customLocation) {
      customLocation.innerHTML = courseDesignationContainer;
      return;
    }
  }

  if (courseData.display_location === course_designations_locations.ALONGSIDEHEADER && header) {
    const additionalStyles = "display: flex;flex-direction: row;justify-content: space-between;"
      + "align-items: center;gap: 2rem;flex-wrap: wrap;";
    header.setAttribute("style", (header.getAttribute("style") || '') + additionalStyles);
    header.insertAdjacentHTML("beforeend", courseDesignationContainer);

    const headerContainer = mainContent.querySelector('.page-heading');
    if (headerContainer) {
      headerContainer.setAttribute("style", (headerContainer.getAttribute("style") || '') + "width: 100%;");
    }
    return;
  }

  if (courseData.display_location === course_designations_locations.BOTTOMOFPAGE) {
    mainContent.insertAdjacentHTML("beforeend", courseDesignationContainer);
    return;
  }

  mainContent.insertAdjacentHTML("afterbegin", courseDesignationContainer);

  return;
}

function cd_getCourseIdFromUrl() {
  let path = window.location.pathname;
  let courseIdMatch = path.match(/\/courses\/(\d+)/);
  if (courseIdMatch) {
    return courseIdMatch[1];
  }
  return null;
}

// Returns true if path has courses in it and a number followed by it
function cd_isAtCourseHome(courseId) {
  return window.location.pathname === "/courses/" + courseId
}

function cd_isFacultyView() {
  return document.querySelector("#settings-link") !== null;
}

function cd_isPageBeingRefreshed() {
  const navigationEntries = window.performance.getEntriesByType("navigation");
  // If the page was refreshed, we want to update our data in course designations
  // This is done by dumping the old cookie.
  if (navigationEntries.length > 0 && navigationEntries[0].type === "reload") {
    return true;
  }
  return false;
}

async function cd_fetchCourseDesignations(courseId) {
  const hostname = window.location.host;
  let url = `https://canvas-lti.cdl.ucf.edu/course-designations/api/student/get/instance_settings/${courseId}`;
  if (hostname === 'ucf.test.instructure.com') {
    url = `https://canvas-lti.dev.cdl.ucf.edu/course-designations/api/student/get/instance_settings/${courseId}`;
  }

  let dataFromBackend = '';
  let designationsResponse = await fetch(
    url,
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "ngrok-skip-browser-warning": "69420"
      }
    }
  );

  try {
    dataFromBackend = await designationsResponse.text();
    dataFromBackend = JSON.parse(dataFromBackend);
  } catch (e) {
    console.error("Course Designations: Error parsing data from backend:", e);
    return null;
  }

  let value = JSON.stringify(dataFromBackend);

  let key = "course-designations-" + courseId;
  cd_setCourseDesignationsStorage(key, value, 2 * 60 * 60);

  return dataFromBackend;
}

// The entry function for starting the course designations process.
async function cd_checkCourseDesignations() {
  
  const courseId = cd_getCourseIdFromUrl();
  if (!courseId) {
    return;
  }
  
  // Check to see if there is stored data, and if so, use that.
  // However, if the user is on the course home page or if the page is being refreshed,
  // we want to fetch fresh data from the backend and update our local storage with it.
  if (!cd_isAtCourseHome(courseId) && !cd_isPageBeingRefreshed()) {
    let storedData = cd_getCourseDesignationsStorage("course-designations-" + courseId);
    if (storedData) {
      try {
        storedData = JSON.parse(storedData);
        if (storedData?.designations_enabled) {
          cd_placeCourseDesignations(storedData, courseId);
          return;
        }
      } catch (e) {
        console.error("Course Designations: Cannot read stored data. Clearing bad data...", e);
        cd_removeCourseDesignationsStorage("course-designations-" + courseId);
      }
    }
  }

  cd_fetchCourseDesignations(courseId)
    .then((dataFromBackend) => {
      // if the url was valid and the course wants to have designations displayed
      if (dataFromBackend?.designations_enabled) {
        cd_placeCourseDesignations(dataFromBackend, courseId);
      }
    })
    .catch((error) => {
      console.error("Course Designations: Error fetching data from backend:", error);
    });
}

cd_checkCourseDesignations();