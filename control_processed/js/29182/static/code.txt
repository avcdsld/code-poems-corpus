function(){

            var angle = this.state.angular.pos
                ,scratch = Physics.scratchpad()
                ,v = scratch.vector()
                ,aabb = this.geometry.aabb( angle )
                ;

            this.getGlobalOffset( v );

            aabb.x += this.state.pos._[0] + v._[0];
            aabb.y += this.state.pos._[1] + v._[1];

            return scratch.done( aabb );
        }