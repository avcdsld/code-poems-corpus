function(rect) {
        var thisBoundingBox = this.getBoundingBox();
        var otherBoundingBox = rect.getBoundingBox();

        var left = Math.min(thisBoundingBox.x, otherBoundingBox.x);
        var top = Math.min(thisBoundingBox.y, otherBoundingBox.y);
        var right = Math.max(
            thisBoundingBox.x + thisBoundingBox.width,
            otherBoundingBox.x + otherBoundingBox.width);
        var bottom = Math.max(
            thisBoundingBox.y + thisBoundingBox.height,
            otherBoundingBox.y + otherBoundingBox.height);

        return new $.Rect(
            left,
            top,
            right - left,
            bottom - top);
    }