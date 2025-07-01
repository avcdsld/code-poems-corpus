function (element, containerTag) {
    if (element && element.hasChildNodes)
      for (var i = 0; i < element.childNodes.length; ++i)
        if (element.childNodes[i].tagName == containerTag)
          return element.childNodes[i];
  
    return null;
  }