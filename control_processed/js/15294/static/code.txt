function EventContext(ourEvent) {
    this._timeline = [ourEvent];
    this._ourEventIndex = 0;
    this._paginateTokens = {b: null, f: null};

    // this is used by MatrixClient to keep track of active requests
    this._paginateRequests = {b: null, f: null};
}