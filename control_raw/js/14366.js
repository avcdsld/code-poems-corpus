function (map) {
            this._super(me.TMXRenderer, "init", [
                map.cols,
                map.rows,
                map.tilewidth,
                map.tileheight
            ]);
        }