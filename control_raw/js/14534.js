function angleTo(e) {
         var a = this.getBounds();
         var b = e.getBounds(); // the me.Vector2d object also implements the same function, but
         // we have to use here the center of both entities

         var ax = b.pos.x + b.width / 2 - (a.pos.x + a.width / 2);
         var ay = b.pos.y + b.height / 2 - (a.pos.y + a.height / 2);
         return Math.atan2(ay, ax);
       }