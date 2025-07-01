function() {
    var
      tok = this.expect('function'),
      name = tok.val.name;

    // params
    this.state.push('function params');
    this.skipWhitespace();
    var params = this.params();
    this.skipWhitespace();
    this.expect(')');
    this.state.pop();

    // Body
    this.state.push('function');
    var fn = new nodes.Function(name, params);

    fn.column = tok.column;
    fn.lineno = tok.lineno;

    fn.block = this.block(fn);
    this.state.pop();
    return new nodes.Ident(name, fn);
  }