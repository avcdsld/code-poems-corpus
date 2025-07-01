function MongoClient(url, options) {
  if (!(this instanceof MongoClient)) return new MongoClient(url, options);
  // Set up event emitter
  EventEmitter.call(this);

  // The internal state
  this.s = {
    url: url,
    options: options || {},
    promiseLibrary: null,
    dbCache: {},
    sessions: []
  };

  // Get the promiseLibrary
  const promiseLibrary = this.s.options.promiseLibrary || Promise;

  // Add the promise to the internal state
  this.s.promiseLibrary = promiseLibrary;
}