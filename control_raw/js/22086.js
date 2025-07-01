function(trackIds, options, callback) {
    // In case someone is using a version where options parameter did not exist.
    var actualCallback, actualOptions;
    if (typeof options === 'function' && !callback) {
      actualCallback = options;
      actualOptions = {};
    } else {
      actualCallback = callback;
      actualOptions = options;
    }

    return WebApiRequest.builder(this.getAccessToken())
      .withPath('/v1/tracks')
      .withQueryParameters(
        {
          ids: trackIds.join(',')
        },
        actualOptions
      )
      .build()
      .execute(HttpManager.get, actualCallback);
  }