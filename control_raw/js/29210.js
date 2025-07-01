function(){

            parent.recalc.call(this);
            // moment of inertia
            var b
                ,moi = 0
                ;

            for ( var i = 0, l = this.children.length; i < l; i++ ) {
                b = this.children[ i ];
                b.recalc();
                // parallel axis theorem
                moi += b.moi + b.mass * b.state.pos.normSq();
            }

            this.moi = moi;
            return this;
        }