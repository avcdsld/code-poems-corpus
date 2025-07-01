function (response) {
        // res.y >0 means touched by something on the bottom
        // which mean at top position for this one
        if (this.alive && (response.overlapV.y > 0) && response.a.body.falling) {
            // make it dead
            this.alive = false;
            //avoid further collision and delete it
            this.body.setCollisionMask(me.collision.types.NO_OBJECT);
            // set dead animation
            this.renderable.setCurrentAnimation("dead");
            // make it flicker and call destroy once timer finished
            var self = this;
            this.renderable.flicker(750, function () {
                me.game.world.removeChild(self);
            });
            // dead sfx
            me.audio.play("enemykill", false);
            // give some score
            game.data.score += 150;
        }

        return false;
    }