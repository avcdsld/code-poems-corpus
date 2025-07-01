function getLogger(label) {
  let config = defaultConfig

  extend(true, config, module.exports.config)

  let rootLogger = logging.getLogger(chalk.gray(label))

  rootLogger.logLevel = config.loglevel

  return rootLogger
}