function _addEventDispatcherImpl(proto) {
        var temp = {};
        EventDispatcher.makeEventDispatcher(temp);
        proto._on_internal  = temp.on;
        proto._off_internal = temp.off;
        proto.trigger       = temp.trigger;
    }