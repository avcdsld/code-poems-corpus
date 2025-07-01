function(serverResponse, bidRequest) {
    let bid;
    let bids;
    let bidId;
    let bidObj;
    let bidResponses = [];
    let bidsMap = {};

    bids = bidRequest.bidRequest;

    serverResponse = (serverResponse || {}).body;
    for (let i = 0; i < bids.length; i++) {
      bid = {};
      bidObj = bids[i];
      bidId = bidObj.bidId;

      bidsMap[bidId] = bidObj;

      if (serverResponse) {
        const decision = serverResponse.decisions && serverResponse.decisions[bidId];
        const price = decision && decision.pricing && decision.pricing.clearPrice;

        if (decision && price) {
          bid.requestId = bidId;
          bid.cpm = price;
          bid.width = decision.width;
          bid.height = decision.height;
          bid.ad = retrieveAd(bidId, decision);
          bid.currency = 'USD';
          bid.creativeId = decision.adId;
          bid.ttl = 360;
          bid.netRevenue = true;
          bid.referrer = utils.getTopWindowUrl();

          bidResponses.push(bid);
        }
      }
    }

    if (bidResponses.length) {
      window.addEventListener('message', function(e) {
        if (!e.data || e.data.from !== 'ism-bid') {
          return;
        }

        const decision = serverResponse.decisions && serverResponse.decisions[e.data.bidId];
        if (!decision) {
          return;
        }

        const id = 'ism_tag_' + Math.floor((Math.random() * 10e16));
        window[id] = {
          bidId: e.data.bidId,
          serverResponse
        };
        const script = document.createElement('script');
        script.src = 'https://cdn.inskinad.com/isfe/publishercode/' + bidsMap[e.data.bidId].params.siteId + '/default.js?autoload&id=' + id;
        document.getElementsByTagName('head')[0].appendChild(script);
      });
    }

    return bidResponses;
  }