function (e) {
            if (this.dragging === false) {
                this.dragging = true;
                this.grabOffset.set(e.gameX, e.gameY);
                this.grabOffset.sub(this.pos);
                return false;
            }
        }