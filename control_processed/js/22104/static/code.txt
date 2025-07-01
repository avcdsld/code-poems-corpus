function(options, callback) {
    return WebApiRequest.builder(this.getAccessToken())
      .withPath('/v1/me/player/repeat')
      .withQueryParameters({
        state: options.state || 'off'
      })
      .build()
      .execute(HttpManager.put, callback);
  }