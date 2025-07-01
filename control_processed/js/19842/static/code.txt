function _getHost (fauxton_ip) {
    if (fauxton_ip) {
      return fauxton_ip;
    }
    //making some assumptions here
    const interfaces = os.networkInterfaces();
    const eth0 = interfaces[Object.keys(interfaces)[1]];
    return eth0.find(function (item) {
      return item.family === 'IPv4';
    }).address;
  }