function (startX, startY, endX, endY) {
            var context = this.backBufferContext2D;

            if (context < 1 / 255) {
                // Fast path: don't draw fully transparent
                return;
            }

            context.beginPath();
            context.moveTo(startX, startY);
            context.lineTo(endX, endY);
            context.stroke();
        }