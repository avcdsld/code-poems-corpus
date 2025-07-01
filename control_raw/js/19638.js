function(allowedAttributes, exportObject) {
    var definition = this.definition
    var tmp = exportObject || definition.store.utils.clone(this.attributes)

    for (var i in definition.relations) {
      var relation = definition.relations[i]
      if (this['_' + relation.name]) {
        tmp[relation.name] = this['_' + relation.name]
        if (typeof tmp[relation.name].toJson === 'function')
          tmp[relation.name] = tmp[relation.name].toJson()
      }
    }

    if (!allowedAttributes && this.allowedAttributes)
      allowedAttributes = this.allowedAttributes

    for (var name in tmp) {
      if (allowedAttributes && allowedAttributes.indexOf(name) === -1) {
        delete tmp[name]
      } else {
        if (
          definition.attributes &&
          definition.attributes[name] &&
          definition.attributes[name].hidden !== true
        ) {
          tmp[name] = definition.cast(name, tmp[name], 'output', this)

          if (tmp[name] && typeof tmp[name].toJson === 'function'){
            tmp[name] = tmp[name].toJson()
          }

          // convert to external names
          var value = tmp[name]
          delete tmp[name]
          tmp[definition.attributes[name].name] = value
        }
      }
    }

    return tmp
  }