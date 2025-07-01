function scrollHandler(el){
            var state = getState(el);
            return throttle(function(event){
                computeVisibleArea(el);
                computeBarHeight(el); // fallback for an undetected content change
                if (!state.barDragging) {
                    computeBarTop(el);
                    updateDragger(el, {withScrollingClasses: true});
                }
            }.bind(this), state.config.scrollThrottle);
        }