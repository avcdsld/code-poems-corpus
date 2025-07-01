function (globalEasing) {

        var self = this;
        var clipCount = 0;

        var oneTrackDone = function() {
            clipCount--;
            if (clipCount === 0) {
                self._doneCallback();
            }
        };

        var lastClip;
        for (var propName in this._tracks) {
            var clip = createTrackClip(
                this, globalEasing, oneTrackDone,
                this._tracks[propName], propName, self._interpolater, self._maxTime
            );
            if (clip) {
                this._clipList.push(clip);
                clipCount++;

                // If start after added to animation
                if (this.animation) {
                    this.animation.addClip(clip);
                }

                lastClip = clip;
            }
        }

        // Add during callback on the last clip
        if (lastClip) {
            var oldOnFrame = lastClip.onframe;
            lastClip.onframe = function (target, percent) {
                oldOnFrame(target, percent);

                for (var i = 0; i < self._onframeList.length; i++) {
                    self._onframeList[i](target, percent);
                }
            };
        }

        if (!clipCount) {
            this._doneCallback();
        }
        return this;
    }