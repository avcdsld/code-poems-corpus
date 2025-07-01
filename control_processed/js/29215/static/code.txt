function( aabb ){

            if (!aabb) {
                throw 'Error: aabb not set';
            }

            this._edges = {
                min: {
                    x: (aabb.x - aabb.hw),
                    y: (aabb.y - aabb.hh)
                },
                max: {
                    x: (aabb.x + aabb.hw),
                    y: (aabb.y + aabb.hh)
                }
            };

            return this;
        }