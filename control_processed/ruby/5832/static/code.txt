def command(operation, opts = {})
      txn_read_pref = if opts[:session] && opts[:session].in_transaction?
        opts[:session].txn_read_preference
      else
        nil
      end
      txn_read_pref ||= opts[:read] || ServerSelector::PRIMARY
      Lint.validate_underscore_read_preference(txn_read_pref)
      preference = ServerSelector.get(txn_read_pref)

      client.send(:with_session, opts) do |session|
        read_with_retry(session, preference) do |server|
          Operation::Command.new({
            :selector => operation.dup,
            :db_name => name,
            :read => preference,
            :session => session
          }).execute(server)
        end
      end
    end