function bulksDoc (docs, qs0, callback0) {
      const { opts, callback } = getCallback(qs0, callback0)
      return relax({
        db: dbName,
        path: '_bulk_docs',
        body: docs,
        method: 'POST',
        qs: opts
      }, callback)
    }