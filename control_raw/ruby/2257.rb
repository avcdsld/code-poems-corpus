def add_current_transaction_fields(error, transaction)
      return unless transaction

      error.transaction_id = transaction.id
      error.transaction = { sampled: transaction.sampled? }
      error.trace_id = transaction.trace_id
      error.parent_id = ElasticAPM.current_span&.id || transaction.id

      return unless transaction.context

      Util.reverse_merge!(error.context.tags, transaction.context.tags)
      Util.reverse_merge!(error.context.custom, transaction.context.custom)
    end