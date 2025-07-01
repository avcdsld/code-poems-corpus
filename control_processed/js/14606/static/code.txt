function lighten(scale) {
         scale = me.Math.clamp(scale, 0, 1);
         this.glArray[0] = me.Math.clamp(this.glArray[0] + (1 - this.glArray[0]) * scale, 0, 1);
         this.glArray[1] = me.Math.clamp(this.glArray[1] + (1 - this.glArray[1]) * scale, 0, 1);
         this.glArray[2] = me.Math.clamp(this.glArray[2] + (1 - this.glArray[2]) * scale, 0, 1);
         return this;
       }