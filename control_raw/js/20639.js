function TokenInfo(config)
{
  var masterToken;
  var sessionToken;
  var masterTokenExpirationTime;
  var sessionTokenExpirationTime;

  if (Util.isObject(config))
  {
    masterToken                = config.masterToken;
    sessionToken               = config.sessionToken;
    masterTokenExpirationTime  = config.masterTokenExpirationTime;
    sessionTokenExpirationTime = config.sessionTokenExpirationTime;
  }

  /**
   * Returns true if no token-related information is available, false otherwise.
   *
   * @returns {Boolean}
   */
  this.isEmpty = function()
  {
    return !Util.exists(masterToken) ||
        !Util.exists(masterTokenExpirationTime) ||
        !Util.exists(sessionToken) || !Util.exists(sessionTokenExpirationTime);
  };

  /**
   * Clears all token-related information.
   */
  this.clearTokens = function()
  {
    masterToken                = undefined;
    masterTokenExpirationTime  = undefined;
    sessionToken               = undefined;
    sessionTokenExpirationTime = undefined;
  };

  /**
   * Updates the tokens and their expiration times.
   *
   * @param {Object} data
   */
  this.update = function(data)
  {
    masterToken  = data.masterToken;
    sessionToken = data.token || data.sessionToken;

    var currentTime = new Date().getTime();

    masterTokenExpirationTime = currentTime +
        1000 * (data.masterValidityInSeconds || data.validityInSecondsMT);

    sessionTokenExpirationTime = currentTime +
        1000 * (data.validityInSeconds || data.validityInSecondsST);
  };

  /**
   * Returns the master token.
   *
   * @returns {String}
   */
  this.getMasterToken = function()
  {
    return masterToken;
  };

  /**
   * Returns the expiration time of the master token.
   *
   * @returns {Number}
   */
  this.getMasterTokenExpirationTime = function()
  {
    return masterTokenExpirationTime;
  };

  /**
   * Returns the session token.
   *
   * @returns {String}
   */
  this.getSessionToken = function()
  {
    return sessionToken;
  };

  /**
   * Returns the expiration time of the session token.
   *
   * @returns {Number}
   */
  this.getSessionTokenExpirationTime = function()
  {
    return sessionTokenExpirationTime;
  };

  /**
   * Returns a configuration object that can be passed to the TokenInfo
   * constructor to get an equivalent TokenInfo object.
   *
   * @returns {Object}
   */
  this.getConfig = function()
  {
    return {
      masterToken                : masterToken,
      masterTokenExpirationTime  : masterTokenExpirationTime,
      sessionToken               : sessionToken,
      sessionTokenExpirationTime : sessionTokenExpirationTime
    };
  };
}