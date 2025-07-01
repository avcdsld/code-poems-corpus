function(context, font, stroke) {
        context.font = font.font;
        context.fillStyle = font.fillStyle.toRGBA();
        if (stroke === true) {
            context.strokeStyle = font.strokeStyle.toRGBA();
            context.lineWidth = font.lineWidth;
        }
        context.textAlign = font.textAlign;
        context.textBaseline = font.textBaseline;
    }