public boolean isBreakpoint(Message aMessage, boolean isRequest, boolean onlyIfInScope) {
        if (aMessage.isForceIntercept()) {
            // The browser told us to do it Your Honour
            return true;
        }
        
        if (onlyIfInScope && ! aMessage.isInScope()) {
            return false;
        }
        
        if (isBreakOnAllRequests(aMessage, isRequest)) {
            // Break on all requests
            return true;
        } else if (isBreakOnAllResponses(aMessage, isRequest)) {
            // Break on all responses
            return true;
        } else if (isBreakOnStepping(aMessage, isRequest)) {
            // Stopping through all requests and responses
            return true;
        }
        
        return isBreakOnEnabledBreakpoint(aMessage, isRequest, onlyIfInScope);
    }