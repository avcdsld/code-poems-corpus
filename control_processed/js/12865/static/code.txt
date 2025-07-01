function executeDbAdminCommand(db, command, options, callback) {
  db.s.topology.command('admin.$cmd', command, options, (err, result) => {
    // Did the user destroy the topology
    if (db.serverConfig && db.serverConfig.isDestroyed()) {
      return callback(new MongoError('topology was destroyed'));
    }

    if (err) return handleCallback(callback, err);
    handleCallback(callback, null, result.result);
  });
}