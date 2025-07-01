function(options, callback) {
    return WebApiRequest.builder(this.getAccessToken())
      .withPath('/v1/me/player')
      .withHeaders({ 'Content-Type': 'application/json' })
      .withBodyParameters({
        device_ids: options.deviceIds,
        play: !!options.play
      })
      .build()
      .execute(HttpManager.put, callback);
  }