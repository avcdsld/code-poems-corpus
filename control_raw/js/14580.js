function scaleCanvas(scaleX, scaleY) {
         var w = this.canvas.width * scaleX;
         var h = this.canvas.height * scaleY; // adjust CSS style for High-DPI devices

         if (me.device.devicePixelRatio > 1) {
           this.canvas.style.width = w / me.device.devicePixelRatio + "px";
           this.canvas.style.height = h / me.device.devicePixelRatio + "px";
         } else {
           this.canvas.style.width = w + "px";
           this.canvas.style.height = h + "px";
         }

         this.compositor.setProjection(this.canvas.width, this.canvas.height);
       }