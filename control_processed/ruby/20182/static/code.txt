def run(*args)
      session, run_in_tx = session_and_run_in_tx_from_args(args)

      fail ArgumentError, 'Expected a block to run in Transaction.run' unless block_given?

      return yield(nil) unless run_in_tx

      tx = Neo4j::Transaction.new(session)
      yield tx
    rescue Exception => e # rubocop:disable Lint/RescueException
      # print_exception_cause(e)

      tx.mark_failed unless tx.nil?
      raise e
    ensure
      tx.close unless tx.nil?
    end