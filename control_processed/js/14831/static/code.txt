function HKP(keyServerBaseUrl) {
  this._baseUrl = keyServerBaseUrl || config.keyserver;
  this._fetch = typeof window !== 'undefined' ? window.fetch : require('node-fetch');
}