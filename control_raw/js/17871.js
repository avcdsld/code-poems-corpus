function CodeRequest(callContext, authenticationContext, clientId, resource) {
    this._log = new Logger('DeviceCodeRequest', callContext._logContext);
    this._callContext = callContext;
    this._authenticationContext = authenticationContext;
    this._resource = resource;
    this._clientId = clientId;
    
    // This should be set at the beginning of getToken
    // functions that have a userId.
    this._userId = null;
}