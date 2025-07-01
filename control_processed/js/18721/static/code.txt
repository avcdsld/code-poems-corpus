function(zone, callback) {
    var self = this,
        zoneId = zone instanceof dns.Zone ? zone.id : zone;

    var requestOptions = {
      path: urlJoin(_urlPrefix, zoneId, 'subdomains'),
      method: 'GET'
    };

    self._request(requestOptions, function(err, body, res) {
      return err
        ? callback(err)
        : callback(null, body.domains.map(function (result) {
        return new dns.Zone(self, result);
      }), res);
    });
  }