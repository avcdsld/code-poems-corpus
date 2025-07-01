function (x, y, width, height) {
            var color = this.currentColor.clone();
            this.currentColor.copy("#000000");
            this.fillRect(x, y, width, height);
            this.currentColor.copy(color);
            me.pool.push(color);
        }