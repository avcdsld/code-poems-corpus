function (renderer) {
        renderer.setColor(this.color);
        renderer.fillRect(0, 0, this.width, this.height);
        this.font.draw(renderer, this.text, 0, 0);
    }