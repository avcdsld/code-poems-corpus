function (data, fn) {
    data.streamingKey = this.createStreamingKey(data.url, data.revision);
    this.store.setBin(data, function (err, id) {
      data.id = id;
      fn(err || null, err ? undefined : data);
    });
  }