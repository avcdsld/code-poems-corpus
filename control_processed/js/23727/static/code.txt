function saveRect(type, rects, color) {
  let svg = findSVGAtPoint(rects[0].left, rects[0].top);
  let node;
  let annotation;

  if (!svg) {
    return;
  }

  let boundingRect = svg.getBoundingClientRect();

  if (!color) {
    if (type === 'highlight') {
      color = 'FFFF00';
    } else if (type === 'strikeout') {
      color = 'FF0000';
    }
  }

  // Initialize the annotation
  annotation = {
    type,
    color,
    rectangles: [...rects].map((r) => {
      let offset = 0;

      if (type === 'strikeout') {
        offset = r.height / 2;
      }

      return scaleDown(svg, {
        y: (r.top + offset) - boundingRect.top,
        x: r.left - boundingRect.left,
        width: r.width,
        height: r.height
      });
    }).filter((r) => r.width > 0 && r.height > 0 && r.x > -1 && r.y > -1)
  };
  
  // Short circuit if no rectangles exist
  if (annotation.rectangles.length === 0) {
    return;
  }

  // Special treatment for area as it only supports a single rect
  if (type === 'area') {
    let rect = annotation.rectangles[0];
    delete annotation.rectangles;
    annotation.x = rect.x;
    annotation.y = rect.y;
    annotation.width = rect.width;
    annotation.height = rect.height;
  }

  let { documentId, pageNumber } = getMetadata(svg);

  // Add the annotation
  PDFJSAnnotate.getStoreAdapter().addAnnotation(documentId, pageNumber, annotation)
    .then((annotation) => {
      appendChild(svg, annotation);
    });
}