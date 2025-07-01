function(levelTag, message, bufferMaxLength)
  {
    // initialize the winston logger if needed
    if (!winstonLogger)
    {
      winstonLogger = new winston.createLogger(
      {
        transports:
        [
          new (winston.transports.Console)(),
          new (winston.transports.File)({ filename: 'snowflake.log' })
        ],
        level: common.getLevelTag(),
        levels: common.getLevelTagsMap()
      });
    }

    // get the appropriate logging method using the level tag and use this
    // method to log the message
    winstonLogger[levelTag](message);
  }