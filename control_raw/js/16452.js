function triggerGesture(element, startPos, startTouches, gesture, done) {
            var interval = 10,
                loops = Math.ceil(gesture.duration / interval),
                loop = 1;

            function gestureLoop() {
                // calculate the radius
                var radius = gesture.radius;
                if (gesture.scale !== 1) {
                    radius = gesture.radius - (gesture.radius * (1 - gesture.scale) * (1 / loops * loop));
                }

                // calculate new position/rotation
                var posX = startPos[0] + (gesture.distanceX / loops * loop),
                    posY = startPos[1] + (gesture.distanceY / loops * loop),
                    rotation = typeof gesture.rotation == 'number' ? (gesture.rotation / loops * loop) : null,
                    touches = getTouches([posX, posY], startTouches.length, radius, rotation),
                    isFirst = (loop == 1),
                    isLast = (loop == loops);

                if (isFirst) {
                    triggerTouch(touches, element, 'start');
                } else if (isLast) {
                    triggerTouch(touches, element, 'end');
                    return done(touches);
                } else {
                    triggerTouch(touches, element, 'move');
                }

                setTimeout(gestureLoop, interval);
                loop++;
            }
            gestureLoop();
        }