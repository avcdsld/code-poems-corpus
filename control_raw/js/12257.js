function(syncOptions) {
    if (syncOptions.pixelEnabled) {
      return [{
        type: 'image',
        url: spec.SYNC_ENDPOINT1
      },
      {
        type: 'image',
        url: spec.SYNC_ENDPOINT2
      },
      {
        type: 'image',
        url: spec.SYNC_ENDPOINT3
      },
      {
        type: 'image',
        url: spec.SYNC_ENDPOINT4
      }];
    }
  }