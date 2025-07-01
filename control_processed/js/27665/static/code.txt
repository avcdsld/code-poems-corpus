function announce (server, service) {
  var delay = 1000
  var packet = service._records()

  server.register(packet)

  ;(function broadcast () {
    // abort if the service have or is being stopped in the meantime
    if (!service._activated || service._destroyed) return

    server.mdns.respond(packet, function () {
      // This function will optionally be called with an error object. We'll
      // just silently ignore it and retry as we normally would
      if (!service.published) {
        service._activated = true
        service.published = true
        service.emit('up')
      }
      delay = delay * REANNOUNCE_FACTOR
      if (delay < REANNOUNCE_MAX_MS && !service._destroyed) {
        setTimeout(broadcast, delay).unref()
      }
    })
  })()
}