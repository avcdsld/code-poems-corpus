function (/* dt */) {
            // update the velocity
            this.computeVelocity(this.vel);

            // update the body ancestor position
            this.ancestor.pos.add(this.vel);

            // returns true if vel is different from 0
            return (this.vel.x !== 0 || this.vel.y !== 0);
        }