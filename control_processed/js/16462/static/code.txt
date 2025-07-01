function register (server, options, next) {
  server.ext('onPreHandler', function maybeForceGzip (request, reply) {
    if (request.query.force_gzip === 'true') {
      request.info.acceptEncoding = 'gzip'
    }
    reply.continue()
  })

  next()
}