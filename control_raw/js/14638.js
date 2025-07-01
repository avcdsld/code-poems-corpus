function update(dt) {
         // move things forward independent of the current frame rate
         var skew = dt * this._deltaInv; // Decrease particle life

         this.life = this.life > dt ? this.life - dt : 0; // Calculate the particle Age Ratio

         var ageRatio = this.life / this.startLife; // Resize the particle as particle Age Ratio

         var scale = this.startScale;

         if (this.startScale > this.endScale) {
           scale *= ageRatio;
           scale = scale < this.endScale ? this.endScale : scale;
         } else if (this.startScale < this.endScale) {
           scale /= ageRatio;
           scale = scale > this.endScale ? this.endScale : scale;
         } // Set the particle opacity as Age Ratio


         this.alpha = ageRatio; // Adjust the particle velocity

         this.vel.x += this.wind * skew;
         this.vel.y += this.gravity * skew; // If necessary update the rotation of particle in accordance the particle trajectory

         var angle = this.followTrajectory ? Math.atan2(this.vel.y, this.vel.x) : this.angle;
         this.pos.x += this.vel.x * skew;
         this.pos.y += this.vel.y * skew; // Update particle transform

         this.currentTransform.setTransform(scale, 0, 0, 0, scale, 0, this.pos.x, this.pos.y, 1).rotate(angle); // Return true if the particle is not dead yet

         return (this.inViewport || !this.onlyInViewport) && this.life > 0;
       }