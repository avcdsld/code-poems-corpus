public Val lookup(String id) {
    // Lexically scoped functions first
    Val val = _scope == null ? null : _scope.lookup(id);
    if (val != null) return val;

    // disallow TRUE/FALSE/NA to be overwritten by keys in the DKV... just way way saner this way
    if (CONSTS.containsKey(id)) {
      return CONSTS.get(id).exec(this);
    }

    // Now the DKV
    Value value = DKV.get(Key.make(expand(id)));
    if (value != null) {
      if (value.isFrame())
        return addGlobals((Frame) value.get());
      if (value.isModel())
        return new ValModel((Model) value.get());
      // Only understand Frames right now
      throw new IllegalArgumentException("DKV name lookup of " + id + " yielded an instance of type " + value.className() + ", but only Frame & Model are supported");
    }

    // Now the built-ins
    AstPrimitive ast = PRIMS.get(id);
    if (ast != null)
      return new ValFun(ast);

    throw new IllegalArgumentException("Name lookup of '" + id + "' failed");
  }