def query(database, collection, selector, options = {})
      read(Protocol::Query.new(database, collection, selector, options))
    end