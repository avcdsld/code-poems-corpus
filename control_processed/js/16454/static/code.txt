function doubletap(position, element, done) {
                touchTypes.tap(position, element, function() {
                    setTimeout(function() {
                        touchTypes.tap(position, element, done);
                    }, 30);
                });
            }