function (events, fn) {
        if (!this._eventHandlers) {
            return this;
        }

        var eventsList = events.split(/\s+/).map(splitNs),
            i;

        var removeAllMatches = function (eventRec, eventName) {
            var handlerList = this._eventHandlers[eventName],
                k;
            if (!handlerList) {
                return;
            }

            // Walk backwards so it's easy to remove items
            for (k = handlerList.length - 1; k >= 0; k--) {
                // Look at ns & fn only - doRemove() has already taken care of eventName
                if (!eventRec.ns || eventRec.ns === handlerList[k].ns) {
                    var handler = handlerList[k].handler;
                    if (!fn || fn === handler || fn._eventOnceWrapper === handler) {
                        handlerList.splice(k, 1);
                    }
                }
            }
            if (!handlerList.length) {
                delete this._eventHandlers[eventName];
            }
        }.bind(this);

        var doRemove = function (eventRec) {
            if (eventRec.eventName) {
                // If arg calls out an event name, look at that handler list only
                removeAllMatches(eventRec, eventRec.eventName);
            } else {
                // If arg only gives a namespace, look at handler lists for all events
                _.forEach(this._eventHandlers, function (handlerList, eventName) {
                    removeAllMatches(eventRec, eventName);
                });
            }
        }.bind(this);

        // Detach listener for each event clause
        // Each clause may be: bare eventname, bare .namespace, full eventname.namespace
        for (i = 0; i < eventsList.length; i++) {
            doRemove(eventsList[i]);
        }

        return this;  // for chaining
    }