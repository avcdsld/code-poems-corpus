function makeRequest(url, callback) {

  // The JSON file that is loaded should be an array of PageInfo:
  var searchDataRequest = new XMLHttpRequest();
  searchDataRequest.onload = function() {
    callback(JSON.parse(this.responseText));
  };
  searchDataRequest.open('GET', url);
  searchDataRequest.send();
}