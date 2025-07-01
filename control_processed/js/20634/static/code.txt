function SnowflakeService(connectionConfig, httpClient, config)
{
  // validate input
  Errors.assertInternal(Util.isObject(connectionConfig));
  Errors.assertInternal(Util.isObject(httpClient));
  Errors.assertInternal(!Util.exists(config) || Util.isObject(config));

  // if a config object was specified, verify
  // that it has all the information we need
  var tokenInfoConfig;
  if (Util.exists(config))
  {
    Errors.assertInternal(Util.isObject(config));
    Errors.assertInternal(Util.isObject(config.tokenInfo));

    tokenInfoConfig = config.tokenInfo;
  }

  // create a new TokenInfo instance
  var tokenInfo = new TokenInfo(tokenInfoConfig);

  // create state objects for all the different states we can be in
  var stateOptions =
  {
    snowflakeService : this,
    httpClient       : httpClient,
    connectionConfig : connectionConfig,
    tokenInfo        : tokenInfo
  };
  var statePristine     = new StatePristine(stateOptions);
  var stateConnecting   = new StateConnecting(stateOptions);
  var stateConnected    = new StateConnected(stateOptions);
  var stateRenewing     = new StateRenewing(stateOptions);
  var stateDisconnected = new StateDisconnected(stateOptions);

  var currentState;

  /**
   * Transitions to a given state.
   *
   * @param {Object} state
   * @param {Object} [transitionContext]
   */
  var transitionTo = function(state, transitionContext)
  {
    // this check is necessary to make sure we don't re-enter a transient state
    // like Renewing when we're already in it
    if (currentState !== state)
    {
      // if we have a current state, exit it; the null check is necessary
      // because the currentState is undefined at bootstrap time when we
      // transition to the first state
      if (currentState)
      {
        currentState.exit();
      }

      // update the current state
      currentState = state;

      // enter the new state
      currentState.enter(transitionContext);
    }
  };

  /**
   * Transitions to the Pristine state.
   *
   * {Object} [transitionContext]
   */
  this.transitionToPristine = function(transitionContext)
  {
    transitionTo(statePristine, transitionContext);
  };

  /**
   * Transitions to the Connecting state.
   *
   * {Object} [transitionContext]
   */
  this.transitionToConnecting = function(transitionContext)
  {
    transitionTo(stateConnecting, transitionContext);
  };

  /**
   * Transitions to the Connected state.
   *
   * {Object} [transitionContext]
   */
  this.transitionToConnected = function(transitionContext)
  {
    transitionTo(stateConnected, transitionContext);
  };

  /**
   * Transitions to the Renewing state.
   *
   * {Object} [transitionContext]
   */
  this.transitionToRenewing = function(transitionContext)
  {
    transitionTo(stateRenewing, transitionContext);
  };

  /**
   * Transitions to the Disconnected state.
   *
   * {Object} [transitionContext]
   */
  this.transitionToDisconnected = function(transitionContext)
  {
    transitionTo(stateDisconnected, transitionContext);

    // clear the tokens because we're in a fatal state and we don't want the
    // tokens to be available via getConfig() anymore
    tokenInfo.clearTokens();
  };

  /**
   * Returns a configuration object that can be passed to the SnowflakeService
   * constructor to get an equivalent SnowflakeService object.
   *
   * @returns {Object}
   */
  this.getConfig = function()
  {
    return {
      tokenInfo: tokenInfo.getConfig()
    };
  };

  /**
   * Establishes a connection to Snowflake.
   *
   * @param {Object} options
   */
  this.connect = function(options)
  {
    new OperationConnect(options).validate().execute();
  };

  /**
   * Issues a connect-continue request to Snowflake.
   *
   * @param {Object} [options]
   */
  this.continue = function(options)
  {
    new OperationContinue(options).validate().execute();
  };

  /**
   * Issues a generic request to Snowflake.
   *
   * @param {Object} options
   */
  this.request = function(options)
  {
    new OperationRequest(options).validate().execute();
  };

  /**
   * Terminates the current connection to Snowflake.
   *
   * @param {Object} options
   */
  this.destroy = function(options)
  {
    new OperationDestroy(options).validate().execute();
  };

  /**
   * Creates a new OperationAbstract.
   *
   * @param {Object} options
   * @constructor
   */
  function OperationAbstract(options)
  {
    this.options = options;
  }

  /**
   * Validates the operation options.
   *
   * @returns {Object} the operation.
   */
  OperationAbstract.prototype.validate = function()
  {
    return this;
  };

  /**
   * Executes the operation.
   */
  OperationAbstract.prototype.execute = function(){};

  /**
   * Creates a new OperationConnect.
   *
   * @param {Object} options
   * @constructor
   */
  function OperationConnect(options)
  {
    OperationAbstract.apply(this, arguments);
  }

  Util.inherits(OperationConnect, OperationAbstract);

  /**
   * @inheritDoc
   */
  OperationConnect.prototype.validate = function()
  {
    // verify that the options object contains a callback function
    var options = this.options;
    Errors.assertInternal(
        (Util.isObject(options) && Util.isFunction(options.callback)));

    return this;
  };

  /**
   * @inheritDoc
   */
  OperationConnect.prototype.execute = function()
  {
    currentState.connect(this.options);
  };

  /**
   * Creates a new OperationContinue.
   *
   * @param {Object} options
   * @constructor
   */
  function OperationContinue(options)
  {
    OperationAbstract.apply(this, arguments);
  }

  Util.inherits(OperationContinue, OperationAbstract);

  /**
   * @inheritDoc
   */
  OperationContinue.prototype.validate = function()
  {
    // verify that the options contain a json object
    var options = this.options;
    Errors.assertInternal(
        Util.isObject(options) && Util.isObject(options.json));

    return this;
  };

  /**
   * @inheritDoc
   */
  OperationContinue.prototype.execute = function()
  {
    currentState.continue(this.options);
  };

  /**
   * Creates a new OperationRequest.
   *
   * @param {Object} options
   * @constructor
   */
  function OperationRequest(options)
  {
    OperationAbstract.apply(this, arguments);
  }

  Util.inherits(OperationRequest, OperationAbstract);

  /**
   * @inheritDoc
   */
  OperationRequest.prototype.validate = function()
  {
    // verify that the options object contains all the necessary information
    var options = this.options;
    Errors.assertInternal(Util.isObject(options));
    Errors.assertInternal(Util.isString(options.method));
    Errors.assertInternal(
        !Util.exists(options.headers) || Util.isObject(options.headers));
    Errors.assertInternal(Util.isString(options.url));
    Errors.assertInternal(
        !Util.exists(options.json) || Util.isObject(options.json));

    return this;
  };

  /**
   * @inheritDoc
   */
  OperationRequest.prototype.execute = function()
  {
    currentState.request(this.options);
  };

  /**
   * Creates a new OperationDestroy.
   *
   * @param {Object} options
   * @constructor
   */
  function OperationDestroy(options)
  {
    OperationAbstract.apply(this, arguments);
  }

  Util.inherits(OperationDestroy, OperationAbstract);

  /**
   * @inheritDoc
   */
  OperationDestroy.prototype.validate = function()
  {
    // verify that the options object contains a callback function
    var options = this.options;
    Errors.assertInternal(Util.isObject(options) &&
        Util.isFunction(options.callback));

    return this;
  };

  /**
   * @inheritDoc
   */
  OperationDestroy.prototype.execute = function()
  {
    // delegate to current state
    currentState.destroy(this.options);
  };

  /* All queued operations will be added to this array */
  var operationQueue = [];

  /**
   * Appends a request operation to the queue.
   *
   * @param {Object} options
   */
  this.enqueueRequest = function(options)
  {
    operationQueue.push(new OperationRequest(options));
  };

  /**
   * Appends a destroy operation to the queue.
   *
   * @param {Object} options
   */
  this.enqueueDestroy = function(options)
  {
    operationQueue.push(new OperationDestroy(options));
  };

  /**
   * Executes all the operations in the queue.
   */
  this.drainOperationQueue = function()
  {
    // execute all the operations in the queue
    for (var index = 0, length = operationQueue.length; index < length; index++)
    {
      operationQueue[index].execute();
    }

    // empty the queue
    operationQueue.length = 0;
  };

  this.isConnected = function()
  {
    return currentState === stateConnected;
  };

  this.getServiceName = function()
  {
    return Parameters.getValue(Parameters.names.SERVICE_NAME);
  };

  this.getClientSessionKeepAlive = function()
  {
    return Parameters.getValue(Parameters.names.CLIENT_SESSION_KEEP_ALIVE);
  };

  this.getClientSessionKeepAliveHeartbeatFrequency = function()
  {
    return Parameters.getValue(Parameters.names.CLIENT_SESSION_KEEP_ALIVE_HEARTBEAT_FREQUENCY);
  };

  // if we don't have any tokens, start out as pristine
  if (tokenInfo.isEmpty())
  {
    this.transitionToPristine();
  }
  else
  {
    // we're already connected
    this.transitionToConnected();
  }
}