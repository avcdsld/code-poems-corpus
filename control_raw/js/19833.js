function sendBeacon(url, callback){
  var self = this,
      img = document.createElement('img'),
      loaded = false;

  img.onload = function() {
    loaded = true;
    if ('naturalHeight' in this) {
      if (this.naturalHeight + this.naturalWidth === 0) {
        this.onerror();
        return;
      }
    } else if (this.width + this.height === 0) {
      this.onerror();
      return;
    }
    if (callback) {
      callback.call(self);
    }
  };
  img.onerror = function() {
    loaded = true;
    if (callback) {
      callback.call(self, 'An error occurred!', null);
    }
  };
  img.src = url + '&c=clv1';
}