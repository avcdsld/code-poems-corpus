function preDraw(renderer) {
         var bounds = this.getBounds();
         var ax = bounds.width * this.anchorPoint.x,
             ay = bounds.height * this.anchorPoint.y; // save context

         renderer.save(); // apply the defined alpha value

         renderer.setGlobalAlpha(renderer.globalAlpha() * this.getOpacity()); // apply flip

         if (this._flip.x || this._flip.y) {
           var dx = this._flip.x ? this.centerX - ax : 0,
               dy = this._flip.y ? this.centerY - ay : 0;
           renderer.translate(dx, dy);
           renderer.scale(this._flip.x ? -1 : 1, this._flip.y ? -1 : 1);
           renderer.translate(-dx, -dy);
         }

         if (this.autoTransform === true && !this.currentTransform.isIdentity()) {
           this.currentTransform.translate(-ax, -ay); // apply the renderable transformation matrix

           renderer.transform(this.currentTransform);
           this.currentTransform.translate(ax, ay);
         } else {
           // translate to the defined anchor point
           renderer.translate(-ax, -ay);
         }

         if (typeof this.mask !== "undefined") {
           renderer.setMask(this.mask);
         }

         if (typeof this.tint !== "undefined") {
           renderer.setTint(this.tint);
         }
       }