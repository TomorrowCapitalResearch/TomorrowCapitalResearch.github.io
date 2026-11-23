/* Progressive enhancement: filter the research-log rows. Without JavaScript every row stays visible. */
(() => {
  'use strict';
  const bar = document.querySelector('[data-log-filters]');
  const list = document.querySelector('[data-log-list]');
  const count = document.querySelector('[data-log-count]');
  if (!bar || !list) return;
  const rows = Array.from(list.querySelectorAll('.log-row'));
  const buttons = Array.from(bar.querySelectorAll('[data-filter]'));
  bar.hidden = false;
  if (count) count.hidden = false;

  const apply = filter => {
    let shown = 0;
    rows.forEach(row => {
      const match = filter === 'all' || row.dataset.status === filter;
      row.hidden = !match;
      if (match) shown += 1;
    });
    buttons.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.filter === filter)));
    if (count) count.textContent = filter === 'all' ? '' : `Showing ${shown} of ${rows.length}`;
  };

  bar.addEventListener('click', event => {
    const button = event.target.closest('[data-filter]');
    if (button) apply(button.dataset.filter);
  });

  // A shared link to one row (for example #se-03) must work even if a filter hides it.
  const reveal = () => {
    const target = location.hash && document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (target && target.classList.contains('log-row') && target.hidden) {
      apply('all');
      target.scrollIntoView();
    }
  };
  window.addEventListener('hashchange', reveal);
  reveal();
})();
