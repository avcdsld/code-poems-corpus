function validate () {
    var this$1 = this;
    var args = [], len = arguments.length;
    while ( len-- ) args[ len ] = arguments[ len ];

    var validators;
    var value;
    var cb;
    var ret = true;

    if (args.length === 3) {
      validators = [args[0]];
      value = args[1];
      cb = args[2];
    } else if (args.length === 2) {
      if (isPlainObject(args[0])) {
        validators = [args[0].validator];
        value = args[0].value || this.getValue();
        cb = args[1];
      } else {
        validators = this._keysCached(this._uid.toString(), this.results);
        value = args[0];
        cb = args[1];
      }
    } else if (args.length === 1) {
      validators = this._keysCached(this._uid.toString(), this.results);
      value = this.getValue();
      cb = args[0];
    } else {
      validators = this._keysCached(this._uid.toString(), this.results);
      value = this.getValue();
      cb = null;
    }

    if (args.length === 3 || (args.length === 2 && isPlainObject(args[0]))) {
      ret = this._validate(validators[0], value, cb);
    } else {
      validators.forEach(function (validator) {
        ret = this$1._validate(validator, value, cb);
      });
    }

    return ret
  }