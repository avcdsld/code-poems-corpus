function( data ){

            var bodies = this.getTargets()
                ,dt = data.dt
                ,body
                ,collisions = []
                ,ret
                ,bounds = this._edges
                ,dummy = this.body
                ,prevContacts = this.prevContacts || {}
                ,contactList = {}
                ,pairHash = Physics.util.pairHash
                ,hash
                ;

            for ( var i = 0, l = bodies.length; i < l; i++ ){

                body = bodies[ i ];

                // only detect dynamic bodies
                if ( body.treatment === 'dynamic' ){

                    ret = checkEdgeCollide( body, bounds, dummy );

                    if ( ret ){
                        hash = pairHash( body.uid, dummy.uid );

                        for ( var j = 0, ll = ret.length; j < ll; j++ ){
                            contactList[ hash ] = true;
                            ret[ j ].collidedPreviously = prevContacts[ hash ];
                        }

                        collisions.push.apply( collisions, ret );
                    }
                }
            }

            this.prevContacts = contactList;

            if ( collisions.length ){

                this._world.emit( this.options.channel, {
                    collisions: collisions
                });
            }
        }