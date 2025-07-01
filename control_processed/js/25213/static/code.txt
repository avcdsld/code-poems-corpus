function(rect) {
            // Truncate to next, lower integer, but don't modify if already integer
            rect._x = Math.floor(rect._x);
            rect._y = Math.floor(rect._y);
            // Ceil to next, higher integer, but don't modify if already integer
            rect._w = Math.ceil(rect._w);
            rect._h = Math.ceil(rect._h);
            return rect;
        }