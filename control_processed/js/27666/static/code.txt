function teardown (server, services, cb) {
  if (!Array.isArray(services)) services = [services]

  services = services.filter(function (service) {
    return service._activated // ignore services not currently starting or started
  })

  var records = flatten.depth(services.map(function (service) {
    service._activated = false
    var records = service._records()
    records.forEach(function (record) {
      record.ttl = 0 // prepare goodbye message
    })
    return records
  }), 1)

  if (records.length === 0) return cb && cb()

  server.unregister(records)

  // send goodbye message
  server.mdns.respond(records, function () {
    services.forEach(function (service) {
      service.published = false
    })
    if (cb) cb.apply(null, arguments)
  })
}