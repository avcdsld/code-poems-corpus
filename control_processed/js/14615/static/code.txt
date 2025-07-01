function update(dt) {
         var duration = 0,
             now = me.timer.getTime(),
             result = false;

         if (this._lastUpdate !== now) {
           this._lastUpdate = now;
           this.animations.forEach(function (anim) {
             anim.dt += dt;
             duration = anim.cur.duration;

             while (anim.dt >= duration) {
               anim.dt -= duration;
               anim.idx = (anim.idx + 1) % anim.frames.length;
               anim.cur = anim.frames[anim.idx];
               duration = anim.cur.duration;
               result = true;
             }
           });
         }

         return result;
       }