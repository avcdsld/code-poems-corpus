function expungeFile(id) {
        delete detachLoadEvents[id];

        // If we are dealing with CORS, we might still be waiting for a response from a loaded iframe.
        // In that case, terminate the timer waiting for a message from the loaded iframe
        // and stop listening for any more messages coming from this iframe.
        if (isCors) {
            clearTimeout(postMessageCallbackTimers[id]);
            delete postMessageCallbackTimers[id];
            corsMessageReceiver.stopReceivingMessages(id);
        }

        var iframe = document.getElementById(handler._getIframeName(id));
        if (iframe) {
            // To cancel request set src to something else.  We use src="javascript:false;"
            // because it doesn't trigger ie6 prompt on https
            /* jshint scripturl:true */
            iframe.setAttribute("src", "javascript:false;");

            qq(iframe).remove();
        }
    }