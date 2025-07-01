function( force, p ){

            if ( this.treatment !== 'dynamic' ){
                return this;
            }

            var scratch = Physics.scratchpad()
                ,r = scratch.vector()
                ,state
                ;

            // if no point at which to apply the force... apply at center of mass
            if ( p && this.moi ){

                // apply torques
                state = this.state;
                r.clone( p );
                // r cross F
                this.state.angular.acc -= r.cross( force ) / this.moi;
            }

            this.accelerate( r.clone( force ).mult( 1/this.mass ) );

            scratch.done();
            return this;
        }