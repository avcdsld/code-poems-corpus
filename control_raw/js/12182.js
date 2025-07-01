function(bid) {
    return bid.params && (!!bid.params.placementId || (!!bid.params.minCPM && !!bid.params.minCPC));
  }