function indexes(coll, options, callback) {
  options = Object.assign({}, { full: true }, options);
  indexInformationDb(coll.s.db, coll.s.name, options, callback);
}