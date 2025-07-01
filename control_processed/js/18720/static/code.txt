function (zone, options, callback) {
    var self = this,
        zoneId = zone instanceof dns.Zone ? zone.id : zone;

    if (typeof(options) === 'function') {
      callback = options;
      options = {};
    }

    var requestOptions = {
      path: urlJoin(_urlPrefix, zoneId, 'clone'),
      method: 'POST',
      qs: {
        cloneName: options.cloneName
      }
    };

    _.extend(requestOptions.qs, _.pick(options, ['cloneSubdomains', 'modifyComment',
    'modifyEmailAddress', 'modifyRecordData']));

    self._asyncRequest(requestOptions, function (err, result) {
      return err
        ? callback(err)
        : callback(err, result.response.domains.map(function (domain) {
        return new dns.Zone(self, domain);
      })[0]);
    });
  }