function(options) {
    this.autojoin = options || {}
    this.autojoin.enabled = true
    this.autojoin.relations = this.autojoin.relations || []
    return this
  }