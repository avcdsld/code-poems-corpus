function LogicalType(schema, opts) {
  this._logicalTypeName = schema.logicalType;
  Type.call(this);
  LOGICAL_TYPE = this;
  try {
    this._underlyingType = Type.forSchema(schema, opts);
  } finally {
    LOGICAL_TYPE = null;
    // Remove the underlying type now that we're done instantiating. Note that
    // in some (rare) cases, it might not have been inserted; for example, if
    // this constructor was manually called with an already instantiated type.
    var l = UNDERLYING_TYPES.length;
    if (l && UNDERLYING_TYPES[l - 1][0] === this) {
      UNDERLYING_TYPES.pop();
    }
  }
  // We create a separate branch constructor for logical types to keep them
  // monomorphic.
  if (Type.isType(this.underlyingType, 'union')) {
    this._branchConstructor = this.underlyingType._branchConstructor;
  } else {
    this._branchConstructor = this.underlyingType._createBranchConstructor();
  }
  // We don't freeze derived types to allow arbitrary properties. Implementors
  // can still do so in the subclass' constructor at their convenience.
}