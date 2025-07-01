function onMessage(obj) {
    var id = obj.id;
    if (!self._matchesPrefix(id)) {
      debug('discarding unscoped message %s', id);
      return;
    }
    var cb = self._registry.get(id);
    if (cb) {
      process.nextTick(function () {
        debug('received message %s', id);
        // Ensure that the initial callback gets called asynchronously, even
        // for completely synchronous transports (otherwise the number of
        // pending requests will sometimes be inconsistent between stateful and
        // stateless transports).
        cb(null, Buffer.concat(obj.payload), self._adapter);
      });
    }
  }