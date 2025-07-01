function toggleSubmenu(trigger, toggleFn) {
    const droplet = document.getElementById(trigger.getAttribute('aria-controls'));

    if (!droplet) { return; }

    toggleFn(droplet, (noFocus, focusTarget) => {
      const prevExpanded = droplet.getAttribute('aria-expanded');
      const wasCollapsed = !prevExpanded || prevExpanded === 'false';
      droplet.setAttribute('aria-expanded', wasCollapsed ? 'true' : 'false');

      if (focusTarget) {
        focusTarget.focus();
      } else if (!noFocus) {
        let active = queryAll('.dqpl-menuitem-selected', droplet).filter(isVisible);
        active = active.length ?
          active :
          queryAll('[role="menuitem"][tabindex="0"]', droplet).filter(isVisible);
        let focusMe = wasCollapsed ? active[0] : closest(droplet, '[aria-controls][role="menuitem"]');
        focusMe = focusMe || elements.trigger;
        if (focusMe) { focusMe.focus(); }
      }
    });
  }