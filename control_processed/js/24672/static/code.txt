function startHandler(evt) {
        startHandlerOriginal.call(this, evt);
        // must be a picture, only one picture!!
        var node = this.els[1].querySelector('img:first-child');
        var device = this.deviceEvents;
        if (device.hasTouch && node !== null) {
            IN_SCALE_MODE = true;
            var transform = getComputedTranslate(node);
            startTouches = getTouches(evt.targetTouches);
            startX = transform.translateX - 0;
            startY = transform.translateY - 0;
            currentScale = transform.scaleX;
            zoomNode = node;
            var pos = getPosition(node);
            if (evt.targetTouches.length == 2) {
                lastTouchStart = null;
                var touches = evt.touches;
                var touchCenter = getCenter({
                    x: touches[0].pageX,
                    y: touches[0].pageY
                }, {
                    x: touches[1].pageX,
                    y: touches[1].pageY
                });
                node.style.webkitTransformOrigin = generateTransformOrigin(touchCenter.x - pos.left, touchCenter.y - pos.top);
            } else if (evt.targetTouches.length === 1) {
                var time = (new Date()).getTime();
                gesture = 0;
                if (time - lastTouchStart < 300) {
                    evt.preventDefault();
                    gesture = 3;
                }
                lastTouchStart = time;
            }
        }
    }