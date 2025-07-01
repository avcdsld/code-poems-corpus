function buildImp(bidRequest, secure) {
  const imp = {
    'id': bidRequest.bidId,
    'tagid': bidRequest.adUnitCode
  };

  if (utils.deepAccess(bidRequest, `mediaTypes.banner`)) {
    let sizes = canonicalizeSizesArray(bidRequest.mediaTypes.banner.sizes);
    imp.banner = {
      format: sizes.map(s => ({'w': s[0], 'h': s[1]})),
      topframe: 0
    };
  } else if (utils.deepAccess(bidRequest, 'mediaTypes.video')) {
    let size = canonicalizeSizesArray(bidRequest.mediaTypes.video.playerSize)[0];
    imp.video = {
      w: size[0],
      h: size[1]
    };
    if (bidRequest.params.video) {
      Object.keys(bidRequest.params.video)
        .filter(param => includes(VIDEO_TARGETING, param))
        .forEach(param => imp.video[param] = bidRequest.params.video[param]);
    }
  }
  if (secure) {
    imp.secure = 1;
  }
  return imp;
}