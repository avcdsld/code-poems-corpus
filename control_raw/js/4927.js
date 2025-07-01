function _addListener(type, handler) {
        if (_status[type]) {
            _callHandler(handler);
        } else {
            _callbacks[type].push(handler);
        }
    }