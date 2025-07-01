function(options) {
    if (!options) {
      options = {};
    }

    if (options.log) {
      if (!_.isFunction(options.log)) {
        throw new Error('setLogOptions expects the log key in the options parameter to be a function');
      }
    } else {
      // if no log function was passed set it to a default no op function.
      options.log = function() {};
    }

    if (options.level) {
      var level = options.level;
      if (level < 0 || level > 3) {
        throw new Error('setLogOptions expects the level key to be in the range 0 to 3 inclusive');
      }
    } else {
      options.level = this.LOGGING_LEVEL.ERROR;
    }

    if (options.loggingWithPII != true) {
      options.loggingWithPII = false;
    }
    
    this.LogOptions = options;
  }