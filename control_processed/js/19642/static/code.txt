function() {
    var model = this.definition.model
    var collection = model.include.apply(
      model,
      this.definition.store.utils.args(arguments)
    )

    // add the current record to the collection
    collection.addInternal('data_loaded', [this.clearRelations()]) // clear relations for start with a clean record
    collection.first()

    return collection
  }