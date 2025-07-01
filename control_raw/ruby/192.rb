def committed!(should_run_callbacks: true) #:nodoc:
      if should_run_callbacks && trigger_transactional_callbacks?
        @_committed_already_called = true
        _run_commit_without_transaction_enrollment_callbacks
        _run_commit_callbacks
      end
    ensure
      @_committed_already_called = false
      force_clear_transaction_record_state
    end