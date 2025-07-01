function( routine ) {
    var it = this
    var routine = Array.isArray( routine )
      ? routine
      : this.routine

    routine
    .forEach(function( method ) {
      if (
         typeof method === 'string' &&
         typeof it[ method ] === 'function'
      ) {
        it[ method ]()
      } else if (
        Array.isArray( method ) &&
        typeof it[ method[0] ] === 'function'
      ) {
        it[ method.shift() ].apply( it, method )
      }
    })
    return this
  }