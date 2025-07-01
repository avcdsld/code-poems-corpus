function Session(options) {
  options = options || {};
  this.id = options.id || this._guid();
  this.parent = options.parent || undefined;
  this.authenticating = options.authenticating || false;
  this.authenticated = options.authenticated || undefined;
  this.user = options.user || 'guest';
  this.host = options.host;
  this.address = options.address || undefined;
  this._isLocal = options.local || undefined;
  this._delimiter = options.delimiter || String(os.hostname()).split('.')[0] + '~$';
  this._modeDelimiter = undefined;

  // Keeps history of how many times in a row `tab` was
  // pressed on the keyboard.
  this._tabCtr = 0;

  this.cmdHistory = this.parent.cmdHistory;

  // Special command mode vorpal is in at the moment,
  // such as REPL. See mode documentation.
  this._mode = undefined;

  return this;
}