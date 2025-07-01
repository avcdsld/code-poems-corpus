function(index) {
    var self = this.chain()

    if (typeof index !== 'number') {
      index = self.indexOf(index)
    }

    const record = self[index]
    var relation = self.getInternal('relation')
    var parentRecord = self.getInternal('relation_to')

    if (
      record &&
      relation &&
      parentRecord &&
      typeof relation.remove === 'function'
    ) {
      relation.remove.call(self, parentRecord, record)
    }

    self.splice(index, 1)

    return self
  }