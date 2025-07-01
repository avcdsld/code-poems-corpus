function splitNs(eventStr) {
        var dot = eventStr.indexOf(".");
        if (dot === -1) {
            return { eventName: eventStr };
        } else {
            return { eventName: eventStr.substring(0, dot), ns: eventStr.substring(dot) };
        }
    }