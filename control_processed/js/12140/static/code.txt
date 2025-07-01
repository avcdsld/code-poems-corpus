function(validBidRequests) {
    // Do we need to group by bidder? i.e. to make multiple requests for
    // different endpoints.

    let ret = {
      method: 'POST',
      url: '',
      data: '',
      bidRequest: []
    };

    if (validBidRequests.length < 1) {
      return ret;
    }

    let ENDPOINT_URL;

    // These variables are used in creating the user sync URL.
    siteId = validBidRequests[0].params.siteId;
    bidder = validBidRequests[0].bidder;

    const data = Object.assign({
      placements: [],
      time: Date.now(),
      user: {},
      url: utils.getTopWindowUrl(),
      referrer: document.referrer,
      enableBotFiltering: true,
      includePricingData: true,
      parallel: true
    }, validBidRequests[0].params);

    validBidRequests.map(bid => {
      let config = CONFIG[bid.bidder];
      ENDPOINT_URL = config.BASE_URI;

      const placement = Object.assign({
        divName: bid.bidId,
        adTypes: bid.adTypes || getSize(bid.sizes)
      }, bid.params);

      if (placement.networkId && placement.siteId) {
        data.placements.push(placement);
      }
    });

    ret.data = JSON.stringify(data);
    ret.bidRequest = validBidRequests;
    ret.url = ENDPOINT_URL;

    return ret;
  }