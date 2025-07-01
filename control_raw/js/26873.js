function loadConfig(configPath, input) {
  let config
  if (configPath.endsWith('.yml') || configPath.endsWith('.yaml')) {
    config = loadYAMLConfig(configPath)
  } else {
    config = loadJSConfig(configPath)
  }

  if (isUndefined(config)) {
    // let the caller deal with this
    return config
  }
  let typeMessage = `Your config data type was`
  if (isFunction(config)) {
    config = config(input)
    typeMessage = `${typeMessage} a function which returned`
  }
  const emptyConfig = isEmpty(config)
  const plainObjectConfig = isPlainObject(config)
  if (plainObjectConfig && emptyConfig) {
    typeMessage = `${typeMessage} an object, but it was empty`
  } else {
    typeMessage = `${typeMessage} a data type of "${typeOf(config)}"`
  }
  if (!plainObjectConfig || emptyConfig) {
    log.error({
      message: chalk.red(
        oneLine`
          The package-scripts configuration
          ("${configPath.replace(/\\/g, '/')}") must be a non-empty object
          or a function that returns a non-empty object.
        `,
      ),
      ref: 'config-must-be-an-object',
    })
    throw new Error(typeMessage)
  }

  const defaultConfig = {
    options: {
      'help-style': 'all',
    },
  }

  return {...defaultConfig, ...config}
}