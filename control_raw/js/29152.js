function( topic, fn, scope ){

            var listeners
                ,listn
                ;

            if ( !this._topics ){
                // nothing subscribed
                return this;
            }

            if ( topic === true ){
                // purge all listeners
                this._topics = {};
                return this;
            }

            // check if we're subscribing to multiple topics
            // with an object
            if ( Physics.util.isObject( topic ) ){

                for ( var t in topic ){

                    this.off( t, topic[ t ] );
                }

                return this;
            }

            listeners = this._topics[ topic ];

            if (!listeners){
                return this;
            }

            if ( fn === true ){
                // purge all listeners for topic
                this._topics[ topic ] = [];
                return this;
            }

            for ( var i = 0, l = listeners.length; i < l; i++ ){

                listn = listeners[ i ];

                if (
                    (listn._bindfn_ === fn || listn === fn) &&
                    ( (!scope) || listn._scope_ === scope) // check the scope too if specified
                ){
                    listeners.splice( i, 1 );
                    break;
                }
            }

            return this;
        }