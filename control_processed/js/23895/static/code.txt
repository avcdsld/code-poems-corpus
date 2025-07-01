function V1(domain) {
  Version.prototype.constructor.call(this, domain, 'v1');

  // Resources
  this._compositionHooks = undefined;
  this._compositionSettings = undefined;
  this._recordings = undefined;
  this._recordingSettings = undefined;
  this._compositions = undefined;
  this._rooms = undefined;
}