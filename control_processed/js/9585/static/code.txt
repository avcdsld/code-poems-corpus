function fixOffset (value) {
    var elements = getElements();

    if (!elements.tabs.length || !ctrl.shouldPaginate) return 0;

    var lastTab    = elements.tabs[ elements.tabs.length - 1 ],
        totalWidth = lastTab.offsetLeft + lastTab.offsetWidth;

    if (isRtl()) {
      value = Math.min(elements.paging.offsetWidth - elements.canvas.clientWidth, value);
      value = Math.max(0, value);
    } else {
      value = Math.max(0, value);
      value = Math.min(totalWidth - elements.canvas.clientWidth, value);
    }

    return value;
  }