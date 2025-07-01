function transform(m) {
         var points = this.points;
         var len = points.length;

         for (var i = 0; i < len; i++) {
           m.multiplyVector(points[i]);
         }

         this.recalc();
         this.updateBounds();
         return this;
       }