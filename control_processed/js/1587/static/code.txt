function load(url, successCallback, errorCallback) {
  const xhr = new XMLHttpRequest();

  // async, however scripts will be executed in the order they are in the
  // DOM to mirror normal script loading.
  xhr.open("GET", url, true);
  if ("overrideMimeType" in xhr) {
    xhr.overrideMimeType("text/plain");
  }
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      if (xhr.status === 0 || xhr.status === 200) {
        successCallback(xhr.responseText);
      } else {
        errorCallback();
        throw new Error("Could not load " + url);
      }
    }
  };
  return xhr.send(null);
}