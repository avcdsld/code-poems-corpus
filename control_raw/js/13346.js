function showMindMap(doc) {
    view.setZoomFactor(zoomController.DEFAULT_ZOOM);
    var dimensions = doc.dimensions;
    view.setDimensions(dimensions.x, dimensions.y);
    var map = doc.mindmap;
    view.drawMap(map);
    view.center();

    mindmapModel.selectNode(map.root);
  }