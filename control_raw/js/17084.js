function(options) {
  this.name = options.name;
  this.isInternal = options.isInternal;
  this.pluginModule = options.pluginModule;
  this.pluginPath = options.pluginPath;
  this.pluginConfig = options.pluginConfig;
  this.shouldInterceptLogs = options.interceptLogs;
  this.clientWeb3Providers = [];
  this.beforeDeploy = [];
  this.contractsGenerators = [];
  this.generateCustomContractCode = null;
  this.testContractFactory = null;
  this.pipeline = [];
  this.pipelineFiles = [];
  this.console = [];
  this.contractsConfigs = [];
  this.contractsFiles = [];
  this.compilers = [];
  this.serviceChecks = [];
  this.dappGenerators = [];
  this.pluginTypes = [];
  this.uploadCmds = [];
  this.apiCalls = [];
  this.imports = [];
  this.embarkjs_code = [];
  this.embarkjs_init_code = {};
  this.embarkjs_init_console_code = {};
  this.afterContractsDeployActions = [];
  this.onDeployActions = [];
  this.eventActions = {};
  this._loggerObject = options.logger;
  this.logger = this._loggerObject; // Might get changed if we do intercept
  this.events = options.events;
  this.config = options.config;
  this.plugins = options.plugins;
  this.fs = options.fs;
  this.env = options.env;
  this.loaded = false;
  this.currentContext = options.context;
  this.acceptedContext = options.pluginConfig.context || [constants.contexts.any];
  this.version = options.version;
  this.constants = constants;

  if (!Array.isArray(this.currentContext)) {
    this.currentContext = [this.currentContext];
  }
  if (!Array.isArray(this.acceptedContext)) {
    this.acceptedContext = [this.acceptedContext];
  }
}