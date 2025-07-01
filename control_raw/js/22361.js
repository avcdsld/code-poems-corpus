function(level, x, y) {
            var num = 0;
            var size = {};

            //Sum up all tiles below the level we want the number of tiles
            for (var z = 0; z < level; z++) {
                size = this.gridSize[z];
                num += size.x * size.y;
            }
            //Add the tiles of the level
            size = this.gridSize[level];
            num += size.x * y + x;
            return num;
        }