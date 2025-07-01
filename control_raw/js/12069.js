function (serverResponse, bidRequests) {
    const body = serverResponse.body;
    if (!body.results || body.results.length < 1) {
      return [];
    }
    const bidRequest = bidRequests.bidRequest;
    const bidResponse = {
      requestId: bidRequest.bidId,
      cpm: body.cpm || 0,
      width: body.w ? body.w : 1,
      height: body.h ? body.h : 1,
      creativeId: body.creativeid || '',
      dealId: body.dealid || '',
      currency: getCurrencyType(),
      netRevenue: true,
      ttl: body.ttl || 10,
    };
    if (isNative(body)) {
      bidResponse.native = createNativeAd(body);
      bidResponse.mediaType = NATIVE;
    } else {
      // banner
      bidResponse.ad = createAd(body, bidRequest);
    }
    return [bidResponse];
  }