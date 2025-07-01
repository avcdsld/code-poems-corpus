function isBidRequestValid(bid) {
  return !(bid.bidder !== BIDDER_CODE || !bid.params || !bid.params.key);
}