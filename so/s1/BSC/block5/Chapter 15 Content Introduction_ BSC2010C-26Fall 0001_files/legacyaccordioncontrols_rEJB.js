// Accordion
var ucfAccordionButtons = $(".ucf-accordion h3>a");

function ucfAccordionClickHandler(e) {
  e.preventDefault();
  $control = $(this);

  accordionContent = $control.attr("aria-controls");
  ucfCheckOtherAccordions($control[0]);

  isAriaExp = $control.attr("aria-expanded");
  newAriaExp = isAriaExp == "false" ? "true" : "false";
  $control.attr("aria-expanded", newAriaExp);

  isAriaHid = $("#" + accordionContent).attr("aria-hidden");
  if (isAriaHid == "true") {
    $("#" + accordionContent).attr("aria-hidden", "false");
    $("#" + accordionContent).addClass("accordion-content-visible");
  } else {
    $("#" + accordionContent).attr("aria-hidden", "true");
    $("#" + accordionContent).removeClass("accordion-content-visible");
  }
}

function ucfAccordionToggle() {
  $(".ucf-accordion .accordion-control").on("click", ucfAccordionClickHandler);

  // Allow spacebar to activate the link
  $(".ucf-accordion .accordion-control").keyup(function (e) {
    if (e.which == 32) {
      e.preventDefault();
      $(this).click();
    }
  });

  // Disable automatic scrolling when spacebar is pressed down
  $(".ucf-accordion .accordion-control").keydown(function (e) {
    if (e.which == 32) {
      e.preventDefault();
      return false;
    }
  });
}

function ucfCheckOtherAccordions(elem) {
  for (var i = 0; i < ucfAccordionButtons.length; i++) {
    if (ucfAccordionButtons[i] != elem) {
      if ($(ucfAccordionButtons[i]).attr("aria-expanded") == "true") {
        $(ucfAccordionButtons[i]).attr("aria-expanded", "false");
        content = $(ucfAccordionButtons[i]).attr("aria-controls");
        $("#" + content).attr("aria-hidden", "true");
        $("#" + content).removeClass("accordion-content-visible");
      }
    }
  }
}

// All code that needs to run when the window is completely done loading should go here
window.addEventListener("load", ucfAccordionInitialize);

function ucfAccordionInitialize(evt) {
  // Initialize accordions if they exist
  ucfAccordionButtons = $(".ucf-accordion h3 > a");
  ucfAccordionToggle();
}