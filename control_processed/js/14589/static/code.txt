function translate(x, y) {
         if (this.settings.subPixel === false) {
           this.currentTransform.translate(~~x, ~~y);
         } else {
           this.currentTransform.translate(x, y);
         }
       }