function updateBoundsPos(newX, newY) {
         var bounds = this.getBounds();
         bounds.pos.set(newX - this.anchorPoint.x * bounds.width, newY - this.anchorPoint.y * bounds.height); // XXX: This is called from the constructor, before it gets an ancestor

         if (this.ancestor instanceof me.Container && !this.floating) {
           bounds.pos.add(this.ancestor._absPos);
         }

         return bounds;
       }