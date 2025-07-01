function HttpClient(connectionConfig)
{
  // save the connection config
  this._connectionConfig = connectionConfig;

  // check that we have a valid request module
  var requestModule = this.getRequestModule();
  Errors.assertInternal(
      Util.isObject(requestModule) || Util.isFunction(requestModule));
}