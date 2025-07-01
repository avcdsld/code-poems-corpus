function mouseMoveRedraw() {
            if (!bezierEditor.dragElement) {
                animationRequest = null;
                return;
            }

            // Update code
            bezierEditor._commitTimingFunction();

            bezierEditor._updateCanvas();
            animationRequest = window.requestAnimationFrame(mouseMoveRedraw);
        }