function(validBidRequests, bidderRequest) {
    const loc = utils.getTopWindowLocation();
    const page = loc.href;
    const isPageSecure = (loc.protocol === 'https:') ? 1 : 0;
    let siteId = '';
    let requestId = '';
    let pubcid = null;

    const conversantImps = validBidRequests.map(function(bid) {
      const bidfloor = utils.getBidIdParameter('bidfloor', bid.params);
      const secure = isPageSecure || (utils.getBidIdParameter('secure', bid.params) ? 1 : 0);

      siteId = utils.getBidIdParameter('site_id', bid.params);
      requestId = bid.auctionId;

      const imp = {
        id: bid.bidId,
        secure: secure,
        bidfloor: bidfloor || 0,
        displaymanager: 'Prebid.js',
        displaymanagerver: VERSION
      };

      copyOptProperty(bid.params.tag_id, imp, 'tagid');

      if (isVideoRequest(bid)) {
        const videoData = utils.deepAccess(bid, 'mediaTypes.video') || {};
        const format = convertSizes(videoData.playerSize || bid.sizes);
        const video = {};

        if (format && format[0]) {
          copyOptProperty(format[0].w, video, 'w');
          copyOptProperty(format[0].h, video, 'h');
        }

        copyOptProperty(bid.params.position, video, 'pos');
        copyOptProperty(bid.params.mimes || videoData.mimes, video, 'mimes');
        copyOptProperty(bid.params.maxduration, video, 'maxduration');
        copyOptProperty(bid.params.protocols || videoData.protocols, video, 'protocols');
        copyOptProperty(bid.params.api || videoData.api, video, 'api');

        imp.video = video;
      } else {
        const bannerData = utils.deepAccess(bid, 'mediaTypes.banner') || {};
        const format = convertSizes(bannerData.sizes || bid.sizes);
        const banner = {format: format};

        copyOptProperty(bid.params.position, banner, 'pos');

        imp.banner = banner;
      }

      if (bid.userId && bid.userId.pubcid) {
        pubcid = bid.userId.pubcid;
      } else if (bid.crumbs && bid.crumbs.pubcid) {
        pubcid = bid.crumbs.pubcid;
      }

      return imp;
    });

    const payload = {
      id: requestId,
      imp: conversantImps,
      site: {
        id: siteId,
        mobile: document.querySelector('meta[name="viewport"][content*="width=device-width"]') !== null ? 1 : 0,
        page: page
      },
      device: getDevice(),
      at: 1
    };

    let userExt = {};

    // Add GDPR flag and consent string
    if (bidderRequest && bidderRequest.gdprConsent) {
      userExt.consent = bidderRequest.gdprConsent.consentString;

      if (typeof bidderRequest.gdprConsent.gdprApplies === 'boolean') {
        payload.regs = {
          ext: {
            gdpr: (bidderRequest.gdprConsent.gdprApplies ? 1 : 0)
          }
        };
      }
    }

    // Add common id if available
    if (pubcid) {
      userExt.fpc = pubcid;
    }

    // Only add the user object if it's not empty
    if (!utils.isEmpty(userExt)) {
      payload.user = {ext: userExt};
    }

    return {
      method: 'POST',
      url: URL,
      data: payload,
    };
  }