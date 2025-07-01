function (bidRequests, bidderRequest) {
    let data = {
      placements: []
    };
    bidRequests.map(bidRequest => {
      let channelCode = parseInt(bidRequest.params.channelCode);
      let network = parseInt(channelCode / 1000000);
      let channel = channelCode % 1000000;
      let dim = getSizes(bidRequest.sizes);
      let placement = {
        id: bidRequest.bidId,
        network: network,
        channel: channel,
        publisher: bidRequest.params.pubId ? bidRequest.params.pubId : 0,
        width: dim[0],
        height: dim[1],
        dimension: bidRequest.params.dimId,
        version: '$prebid.version$',
        keyword: '',
        transactionId: bidRequest.transactionId
      }
      if (bidderRequest && bidderRequest.gdprConsent) {
        if (typeof bidderRequest.gdprConsent.gdprApplies === 'boolean') {
          data.gdpr = Number(bidderRequest.gdprConsent.gdprApplies);
        }
        data.gdpr_consent = bidderRequest.gdprConsent.consentString;
      }
      let dimType = DIM_TYPE[String(bidRequest.params.dimId)]
      if (dimType) {
        placement['renderers'] = [{
          'name': dimType
        }]
      } else { // default to display
        placement['renderers'] = [{
          'name': 'display'
        }]
      }
      data['placements'].push(placement);
    });
    let reqUrl = utils.getTopWindowLocation().protocol === 'http:' ? URL : SECURE_URL;
    return {
      method: 'GET',
      url: reqUrl,
      data: 'g=' + JSON.stringify(data)
    }
  }