function( options ){

            parent.init.call( this );
            this.options.defaults( defaults );
            this.options( options );

            this._distanceConstraints = [];
            this._angleConstraints = [];
        }