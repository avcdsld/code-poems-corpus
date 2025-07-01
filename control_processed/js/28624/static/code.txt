function(self, server, cb) {
  // Measure running time
  var start = new Date().getTime();

  // Emit the server heartbeat start
  emitSDAMEvent(self, 'serverHeartbeatStarted', { connectionId: server.name });

  // Execute ismaster
  // Set the socketTimeout for a monitoring message to a low number
  // Ensuring ismaster calls are timed out quickly
  server.command(
    'admin.$cmd',
    {
      ismaster: true
    },
    {
      monitoring: true,
      socketTimeout: self.s.options.connectionTimeout || 2000
    },
    function(err, r) {
      if (self.state === DESTROYED || self.state === UNREFERENCED) {
        server.destroy({ force: true });
        return cb(err, r);
      }

      // Calculate latency
      var latencyMS = new Date().getTime() - start;
      // Set the last updatedTime
      var hrTime = process.hrtime();
      // Calculate the last update time
      server.lastUpdateTime = hrTime[0] * 1000 + Math.round(hrTime[1] / 1000);

      // We had an error, remove it from the state
      if (err) {
        // Emit the server heartbeat failure
        emitSDAMEvent(self, 'serverHeartbeatFailed', {
          durationMS: latencyMS,
          failure: err,
          connectionId: server.name
        });

        // Remove server from the state
        self.s.replicaSetState.remove(server);
      } else {
        // Update the server ismaster
        server.ismaster = r.result;

        // Check if we have a lastWriteDate convert it to MS
        // and store on the server instance for later use
        if (server.ismaster.lastWrite && server.ismaster.lastWrite.lastWriteDate) {
          server.lastWriteDate = server.ismaster.lastWrite.lastWriteDate.getTime();
        }

        // Do we have a brand new server
        if (server.lastIsMasterMS === -1) {
          server.lastIsMasterMS = latencyMS;
        } else if (server.lastIsMasterMS) {
          // After the first measurement, average RTT MUST be computed using an
          // exponentially-weighted moving average formula, with a weighting factor (alpha) of 0.2.
          // If the prior average is denoted old_rtt, then the new average (new_rtt) is
          // computed from a new RTT measurement (x) using the following formula:
          // alpha = 0.2
          // new_rtt = alpha * x + (1 - alpha) * old_rtt
          server.lastIsMasterMS = 0.2 * latencyMS + (1 - 0.2) * server.lastIsMasterMS;
        }

        if (self.s.replicaSetState.update(server)) {
          // Primary lastIsMaster store it
          if (server.lastIsMaster() && server.lastIsMaster().ismaster) {
            self.ismaster = server.lastIsMaster();
          }
        }

        // Server heart beat event
        emitSDAMEvent(self, 'serverHeartbeatSucceeded', {
          durationMS: latencyMS,
          reply: r.result,
          connectionId: server.name
        });
      }

      // Calculate the staleness for this server
      self.s.replicaSetState.updateServerMaxStaleness(server, self.s.haInterval);

      // Callback
      cb(err, r);
    }
  );
}