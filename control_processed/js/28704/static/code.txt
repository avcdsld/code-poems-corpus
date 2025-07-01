function(events) {
    if (!_.isArray(events)) {
      var errEvtsArrMsg = 'events should be an array!';
      debug(errEvtsArrMsg);
      throw new Error(errEvtsArrMsg);
    }
    var self = this;
    _.each(events, function(evt) {
      self.addEvent(evt);
    });
  }