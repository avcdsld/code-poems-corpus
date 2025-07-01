function(model) {
    this.localStorage().setItem(this.name+"-"+model.id, JSON.stringify(model));
    if (!_.include(this.records, model.id.toString()))
      this.records.push(model.id.toString()); this.save();
    return this.find(model);
  }