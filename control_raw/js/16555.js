function createRespondingStub(object, body) {
  return function() {
    this.args.forEach(function(argSet) {
      setTimeout(argSet[1].bind(null, null, object));
    });
    this.yields(null, object, body);
  };
}