function checkStatus() {
    flushMonitoringOperations(self.queue);

    if (self.queue.length === 0) {
      // Get all the known connections
      var connections = self.availableConnections.concat(self.inUseConnections);

      // Check if we have any in flight operations
      for (var i = 0; i < connections.length; i++) {
        // There is an operation still in flight, reschedule a
        // check waiting for it to drain
        if (connections[i].workItems.length > 0) {
          return setTimeout(checkStatus, 1);
        }
      }

      destroy(self, connections, { force: false }, callback);
      // } else if (self.queue.length > 0 && !this.reconnectId) {
    } else {
      // Ensure we empty the queue
      _execute(self)();
      // Set timeout
      setTimeout(checkStatus, 1);
    }
  }