async function registerHapiSwagger(server, logger, config) {
  const Log = logger.bind('register-hapi-swagger')

  let swaggerOptions = {
    documentationPath: '/',
    host: config.swaggerHost,
    expanded: config.docExpansion,
    swaggerUI: config.enableSwaggerUI,
    documentationPage: config.enableSwaggerUI,
    schemes: config.enableSwaggerHttps ? ['https'] : ['http']
  }

  // if swagger config is defined, use that
  if (config.swaggerOptions) {
    swaggerOptions = { ...swaggerOptions, ...config.swaggerOptions }
  }

  // override some options for safety
  if (!swaggerOptions.info) {
    swaggerOptions.info = {}
  }

  swaggerOptions.info.title = config.appTitle
  swaggerOptions.info.version = config.version
  swaggerOptions.reuseDefinitions = false

  await server.register([
    Inert,
    Vision,
    { plugin: HapiSwagger, options: swaggerOptions }
  ])

  Log.info('hapi-swagger plugin registered')
}