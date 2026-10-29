/* Progressive enhancement only. Every page and link works without JavaScript. */
(() => {
  'use strict';
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-menu]');
  if (toggle && menu) {
    document.documentElement.classList.add('js');
    const setOpen = open => {
      toggle.setAttribute('aria-expanded', String(open));
      toggle.textContent = open ? 'Close' : 'Menu';
      menu.classList.toggle('is-open', open);
    };
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    menu.addEventListener('click', event => { if (event.target.closest('a')) setOpen(false); });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });
    document.addEventListener('click', event => {
      if (!event.target.closest('.site-header')) setOpen(false);
    });
    menu.addEventListener('focusout', () => {
      requestAnimationFrame(() => {
        if (!document.activeElement?.closest('.site-header')) setOpen(false);
      });
    });
    const desktop = window.matchMedia('(min-width: 761px)');
    desktop.addEventListener('change', () => setOpen(false));
  }
  document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
})();
