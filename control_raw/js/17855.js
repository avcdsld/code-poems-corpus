function(node) {
    var sibling = node.firstChild;
    while (sibling && !sibling.data) {
      sibling = sibling.nextSibling;
    }

    return sibling.data ? sibling.data : null;
  }