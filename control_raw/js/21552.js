function detectPortOrSystemd(port) {
  if (systemdSocket) {
    const passedSocketCount = parseInt(process.env.LISTEN_FDS, 10) || 0;

    // LISTEN_FDS contains number of sockets passed by Systemd. At least one
    // must be passed. The sockets are set to file descriptors starting from 3.
    // We just crab the first socket from fd 3 since sqlpad binds only one
    // port.
    if (passedSocketCount > 0) {
      console.log('Using port from Systemd');
      return Promise.resolve({ fd: 3 });
    } else {
      console.error(
        'Warning: Systemd socket asked but not found. Trying to bind port ' +
          port +
          ' manually'
      );
    }
  }

  return detectPort(port);
}