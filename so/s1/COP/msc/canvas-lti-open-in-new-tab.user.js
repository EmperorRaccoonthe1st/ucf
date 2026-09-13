// ==UserScript==
// @name         Canvas LTI: Open Assignment in New Tab
// @namespace    https://github.com/owen
// @version      1.0
// @description  Adds an "Open in New Tab" button next to embedded Canvas LTI assignments (like Knewton Alta) to launch them in a top-level tab with authenticated session.
// @match        https://webcourses.ucf.edu/courses/*/assignments/*
// @match        https://*.instructure.com/courses/*/assignments/*
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function () {
  'use strict';

  const TOOLBAR_ID = 'canvas-lti-newtab-toolbar';

  async function launchInNewTab(btn) {
    const defaultHTML = btn.innerHTML;
    try {
      btn.disabled = true;
      btn.innerHTML = '⏳ Launching...';

      // 1. Extract course and assignment IDs from ENV or URL
      const pathMatch = window.location.pathname.match(/\/courses\/(\d+)\/assignments\/(\d+)/);
      const courseId = window.ENV?.COURSE_ID || pathMatch?.[1];
      const assignmentId = window.ENV?.ASSIGNMENT_ID || pathMatch?.[2];

      if (!courseId || !assignmentId) {
        throw new Error('Could not determine Course or Assignment ID from the page.');
      }

      // 2. Request sessionless launch verifier URL from Canvas API
      const apiRes = await fetch(
        `/api/v1/courses/${courseId}/external_tools/sessionless_launch?assignment_id=${assignmentId}&launch_type=assessment`
      );
      if (!apiRes.ok) {
        throw new Error(`Canvas API error: ${apiRes.status} ${apiRes.statusText}`);
      }
      const launchData = await apiRes.json();

      // 3. Fetch the verifier launch page containing the OAuth signed form
      const verifierRes = await fetch(launchData.url);
      if (!verifierRes.ok) {
        throw new Error(`Verifier fetch error: ${verifierRes.status} ${verifierRes.statusText}`);
      }
      const verifierHtml = await verifierRes.text();

      // 4. Parse the signed LTI POST form and submit into a new tab
      const parser = new DOMParser();
      const doc = parser.parseFromString(verifierHtml, 'text/html');
      const form = doc.getElementById('tool_form');

      if (!form) {
        throw new Error('LTI #tool_form was not found in the launch response.');
      }

      form.target = '_blank';
      form.style.display = 'none';
      document.body.appendChild(form);
      form.submit();
      setTimeout(() => form.remove(), 1000);

      btn.innerHTML = '✓ Launched in New Tab!';
      setTimeout(() => {
        btn.innerHTML = defaultHTML;
        btn.disabled = false;
      }, 2500);
    } catch (err) {
      console.error('[Canvas LTI New Tab]', err);
      btn.innerHTML = '⚠ Launch Failed (Check Console)';
      setTimeout(() => {
        btn.innerHTML = defaultHTML;
        btn.disabled = false;
      }, 3500);
    }
  }

  function toggleFullscreen(iframe) {
    if (!iframe) return;
    if (document.fullscreenElement) {
      document.exitFullscreen();
    } else if (iframe.requestFullscreen) {
      iframe.requestFullscreen();
    } else if (iframe.webkitRequestFullscreen) {
      iframe.webkitRequestFullscreen();
    } else if (iframe.mozRequestFullScreen) {
      iframe.mozRequestFullScreen();
    }
  }

  function createToolbar(iframe) {
    if (document.getElementById(TOOLBAR_ID)) return;

    const toolbar = document.createElement('div');
    toolbar.id = TOOLBAR_ID;
    toolbar.style.cssText = `
      display: flex;
      align-items: center;
      gap: 10px;
      margin: 12px 0 8px 0;
      padding: 8px 12px;
      background: rgba(45, 59, 69, 0.06);
      border: 1px solid rgba(45, 59, 69, 0.15);
      border-radius: 6px;
      width: fit-content;
      box-sizing: border-box;
      font-family: inherit;
    `;

    // New Tab Button
    const newTabBtn = document.createElement('button');
    newTabBtn.type = 'button';
    newTabBtn.className = 'btn btn-primary';
    newTabBtn.style.cssText = `
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      font-weight: 600;
      font-size: 13px;
      cursor: pointer;
      border-radius: 4px;
      background-color: #0073e6;
      color: #ffffff;
      border: none;
      transition: background-color 0.15s ease-in-out;
    `;
    newTabBtn.innerHTML = `
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
        <polyline points="15 3 21 3 21 9"></polyline>
        <line x1="10" y1="14" x2="21" y2="3"></line>
      </svg>
      Open Assignment in New Tab
    `;
    newTabBtn.addEventListener('mouseenter', () => (newTabBtn.style.backgroundColor = '#005bb5'));
    newTabBtn.addEventListener('mouseleave', () => (newTabBtn.style.backgroundColor = '#0073e6'));
    newTabBtn.addEventListener('click', () => launchInNewTab(newTabBtn));

    // Fullscreen Button
    const fsBtn = document.createElement('button');
    fsBtn.type = 'button';
    fsBtn.className = 'btn';
    fsBtn.style.cssText = `
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      font-weight: 500;
      font-size: 13px;
      cursor: pointer;
      border-radius: 4px;
      background-color: #f5f5f5;
      color: #2d3b45;
      border: 1px solid #ccc;
      transition: background-color 0.15s ease-in-out;
    `;
    fsBtn.innerHTML = `
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path>
      </svg>
      Fullscreen Iframe
    `;
    fsBtn.addEventListener('mouseenter', () => (fsBtn.style.backgroundColor = '#e6e6e6'));
    fsBtn.addEventListener('mouseleave', () => (fsBtn.style.backgroundColor = '#f5f5f5'));
    fsBtn.addEventListener('click', () => toggleFullscreen(iframe));

    toolbar.appendChild(newTabBtn);
    toolbar.appendChild(fsBtn);

    // Place toolbar directly above the iframe container
    const container = iframe.closest('.tool_content_wrapper') || iframe.parentElement || iframe;
    container.parentNode.insertBefore(toolbar, container);
  }

  function checkAndInject() {
    if (document.getElementById(TOOLBAR_ID)) return;

    // Selector matching Canvas LTI iframes
    const iframe = document.querySelector(
      'iframe.tool_launch, iframe#tool_content, iframe[data-lti-launch="true"], iframe[src*="knewton"], iframe[title*="Alta"], iframe[title*="Knewton"]'
    );

    if (iframe) {
      createToolbar(iframe);
    }
  }

  // Initial check
  checkAndInject();

  // Observe DOM changes for single-page app dynamic renders
  const observer = new MutationObserver(() => {
    checkAndInject();
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true,
  });
})();
