function _onMessage(message) {
        var response    = JSON.parse(message.data),
            msgRecord   = _messageCallbacks[response.id],
            callback    = msgRecord && msgRecord.callback,
            msgText     = (msgRecord && msgRecord.message) || "No message";

        if (msgRecord) {
            // Messages with an ID are a response to a command, fire callback
            callback(response.result, response.error);
            delete _messageCallbacks[response.id];
        } else if (response.method) {
            // Messages with a method are an event, trigger event handlers
            var domainAndMethod = response.method.split("."),
                domain = domainAndMethod[0],
                method = domainAndMethod[1];

            EventDispatcher.triggerWithArray(exports[domain], method, response.params);
        }

        // Always fire event handlers for all messages/errors
        exports.trigger("message", response);

        if (response.error) {
            exports.trigger("error", response.error, msgText);
        }
    }