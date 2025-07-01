function relayEvents(listener, emitter, events) {
  events.forEach(eventName => listener.on(eventName, event => emitter.emit(eventName, event)));
}