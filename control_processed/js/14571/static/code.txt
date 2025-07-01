function strokeRect(x, y, width, height) {
         if (this.backBufferContext2D.globalAlpha < 1 / 255) {
           // Fast path: don't draw fully transparent
           return;
         }

         this.backBufferContext2D.strokeRect(x, y, width, height);
       }