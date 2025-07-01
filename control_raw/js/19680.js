function() {
    const Utils = this.definition.store.utils
    const self = this.chain()

    const parentRelations = self.getInternal('parent_relations')
    const conditions = Utils.toConditionList(
      Utils.args(arguments),
      Object.keys(self.definition.attributes)
    )

    conditions.forEach(function(cond) {
      if (
        cond.type === 'relation' &&
        !self.definition.relations[cond.relation] &&
        !self.options.polymorph
      ) {
        throw new Error(
          'Can\'t find attribute or relation "' +
            cond.relation +
            '" for ' +
            self.definition.modelName
        )
      }

      if (parentRelations) {
        cond.parents = parentRelations
        if (cond.value && cond.value.$attribute && !cond.value.$parents) {
          cond.value.$parents = parentRelations
        }
      }

      self.addInternal('having', cond)
    })

    return self
  }