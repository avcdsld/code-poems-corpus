function(bid) {
    if (bid.bidder !== BIDDER_CODE || typeof bid.params === 'undefined') {
      return false;
    }

    // Video validations
    if (typeof bid.params.video === 'undefined' || typeof bid.params.video.playerWidth === 'undefined' || typeof bid.params.video.playerHeight == 'undefined' || typeof bid.params.video.mimes == 'undefined') {
      return false;
    }

    // Pub Id validation
    if (typeof bid.params.pubId === 'undefined') {
      return false;
    }

    return true;
  }