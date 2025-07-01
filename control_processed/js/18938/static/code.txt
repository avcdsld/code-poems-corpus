function(query, mongooseQuery, logger) {
    if (query.$exclude) {
      if (!Array.isArray(query.$exclude)) {
        query.$exclude = query.$exclude.split(',')
      }

      mongooseQuery.where({ _id: { $nin: query.$exclude } })
      delete query.$exclude
    }
    return mongooseQuery
  }