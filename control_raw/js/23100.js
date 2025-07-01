function StorageServiceClient(storageAccount, storageAccessKey, host, usePathStyleUri, sas, token) {
  StorageServiceClient['super_'].call(this);

  if(storageAccount && storageAccessKey) {
    // account and key
    this.storageAccount = storageAccount;
    this.storageAccessKey = storageAccessKey;
    this.storageCredentials = new SharedKey(this.storageAccount, this.storageAccessKey, usePathStyleUri);
  } else if (sas) {
    // sas
    this.sasToken = sas;
    this.storageCredentials = new SharedAccessSignature(sas);
  } else if (token) {
    // access token
    this.token = token;
    this.storageCredentials = new TokenSigner(token);
  } else {
    // anonymous
    this.anonymous = true;
    this.storageCredentials = {
      signRequest: function(webResource, callback){
        // no op, anonymous access
        callback(null);
      }
    };
  }

  if(host){
    this.setHost(host);
  }

  this.apiVersion = HeaderConstants.TARGET_STORAGE_VERSION;
  this.usePathStyleUri = usePathStyleUri;

  this._initDefaultFilter();

  /**
   * The logger of the service. To change the log level of the services, set the `[logger.level]{@link Logger#level}`.
   * @name StorageServiceClient#logger
   * @type Logger
   * */
  this.logger = new Logger(Logger.LogLevels.INFO);

  this._setDefaultProxy();

  this.xml2jsSettings = StorageServiceClient._getDefaultXml2jsSettings();
  this.defaultLocationMode = StorageUtilities.LocationMode.PRIMARY_ONLY;
}