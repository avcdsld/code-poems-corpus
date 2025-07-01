function Suite(type, opts) {
  Benchmark.Suite.call(this);

  opts = opts || {};
  this._type = type;
  this._compatibleType = avro.parse(type.getSchema(), {
    typeHook: typeHook,
    wrapUnions: opts.wrapUnions
  });
  this._value = opts.value ? type.fromString(opts.value) : type.random();

  Object.keys(opts).forEach(function (name) {
    if (!name.indexOf('_')) {
      return;
    }
    var fn = this['__' + name];
    if (typeof fn == 'function') {
      this.add(name, fn.call(this, opts[name])); // Add benchmark.
    }
  }, this);
}