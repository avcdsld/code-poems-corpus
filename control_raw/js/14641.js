function (name, index, animationspeed) {
            this.anim[name] = {
                name : name,
                frames : [],
                idx : 0,
                length : 0
            };

            // # of frames
            var counter = 0;

            if (typeof (this.textureAtlas) !== "object") {
                return 0;
            }


            if (index == null) {
                index = [];
                // create a default animation with all frame
                Object.keys(this.textureAtlas).forEach(function (v, i) {
                    index[i] = i;
                });
            }

            // set each frame configuration (offset, size, etc..)
            for (var i = 0, len = index.length; i < len; i++) {
                var frame = index[i];
                var frameObject;
                if (typeof(frame) === "number" || typeof(frame) === "string") {
                    frameObject = {
                        name: frame,
                        delay: animationspeed || this.animationspeed
                    };
                }
                else {
                  frameObject = frame;
                }
                var frameObjectName = frameObject.name;
                if (typeof(frameObjectName) === "number") {
                    if (typeof (this.textureAtlas[frameObjectName]) !== "undefined") {
                        // TODO: adding the cache source coordinates add undefined entries in webGL mode
                        this.anim[name].frames[i] = Object.assign(
                            {},
                            this.textureAtlas[frameObjectName],
                            frameObject
                        );
                        counter++;
                    }
                } else { // string
                    if (this.atlasIndices === null) {
                        throw new Error(
                            "string parameters for addAnimation are not allowed for standard spritesheet based Texture"
                        );
                    } else {
                        this.anim[name].frames[i] = Object.assign(
                            {},
                            this.textureAtlas[this.atlasIndices[frameObjectName]],
                            frameObject
                        );
                        counter++;
                    }
                }
            }
            this.anim[name].length = counter;

            return counter;
        }