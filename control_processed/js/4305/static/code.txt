function _onKeyEvent(instance, event) {
            self.trigger("keyEvent", self, event);  // deprecated
            self.trigger(event.type, self, event);
            return event.defaultPrevented;   // false tells CodeMirror we didn't eat the event
        }