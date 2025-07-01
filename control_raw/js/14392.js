function (body) {
            // update the entity bounds to match with the body bounds
            this.getBounds().resize(body.width, body.height);
            // update the bounds pos
            this.updateBoundsPos(this.pos.x, this.pos.y);
        }