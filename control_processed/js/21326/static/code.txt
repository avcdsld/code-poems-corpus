function(evt) {
    L.DomEvent.stop(evt);
    // undo container transform
    this._path._resetTransform();
    // apply matrix
    this._transformPoints(this._matrix);

    this._path._map
      .off('mousemove', this._onDrag, this)
      .off('mouseup', this._onDragEnd, this);

    // consistency
    this._path.fire('dragend', {
      distance: Math.sqrt(
        L.LineUtil._sqDist(this._dragStartPoint, evt.containerPoint)
      )
    });

    this._matrix = null;
    this._startPoint = null;
    this._dragStartPoint = null;
  }