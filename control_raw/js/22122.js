function() {
            var findShape = this.kityEvent && this.kityEvent.targetShape;
            if (!findShape) return null;
            while (!findShape.minderNode && findShape.container) {
                findShape = findShape.container;
            }
            var node = findShape.minderNode;
            if (node && findShape.getOpacity() < 1) return null;
            return node || null;
        }