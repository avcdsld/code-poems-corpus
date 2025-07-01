function(query, mongooseQuery, logger) {
    const Log = logger.bind()
    if (query.$page) {
      mongooseQuery = this.setPage(query, mongooseQuery, Log)
    } else {
      mongooseQuery = this.setSkip(query, mongooseQuery, Log)
    }

    mongooseQuery = this.setLimit(query, mongooseQuery, Log)

    return mongooseQuery
  }