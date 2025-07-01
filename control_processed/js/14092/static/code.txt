function buildRequestData(searchTerm, maxResults) {
  var requestData = {
    numHits: maxResults,
    fuzzy: {
      maxEdits: 2,
      minLength: 5,
      prefixLength: 2
    }
  };

  if (searchTerm instanceof Array) {
    requestData["addresses"] = searchTerm.map(processAddress);
  } else {
    requestData["addr"] = processAddress(searchTerm);
  }
  return requestData;
}