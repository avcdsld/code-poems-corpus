def transaction_group(transaction)
      { requested_date:   transaction.requested_date,
        local_instrument: transaction.local_instrument,
        sequence_type:    transaction.sequence_type,
        batch_booking:    transaction.batch_booking,
        account:          transaction.creditor_account || account
      }
    end