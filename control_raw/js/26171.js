function Type(schema, opts) {
  var type;
  if (LOGICAL_TYPE) {
    type = LOGICAL_TYPE;
    UNDERLYING_TYPES.push([LOGICAL_TYPE, this]);
    LOGICAL_TYPE = null;
  } else {
    type = this;
  }

  // Lazily instantiated hash string. It will be generated the first time the
  // type's default fingerprint is computed (for example when using `equals`).
  // We use a mutable object since types are frozen after instantiation.
  this._hash = new Hash();
  this.name = undefined;
  this.aliases = undefined;
  this.doc = (schema && schema.doc) ? '' + schema.doc : undefined;

  if (schema) {
    // This is a complex (i.e. non-primitive) type.
    var name = schema.name;
    var namespace = schema.namespace === undefined ?
      opts && opts.namespace :
      schema.namespace;
    if (name !== undefined) {
      // This isn't an anonymous type.
      name = qualify(name, namespace);
      if (isPrimitive(name)) {
        // Avro doesn't allow redefining primitive names.
        throw new Error(f('cannot rename primitive type: %j', name));
      }
      var registry = opts && opts.registry;
      if (registry) {
        if (registry[name] !== undefined) {
          throw new Error(f('duplicate type name: %s', name));
        }
        registry[name] = type;
      }
    } else if (opts && opts.noAnonymousTypes) {
      throw new Error(f('missing name property in schema: %j', schema));
    }
    this.name = name;
    this.aliases = schema.aliases ?
      schema.aliases.map(function (s) { return qualify(s, namespace); }) :
      [];
  }
}