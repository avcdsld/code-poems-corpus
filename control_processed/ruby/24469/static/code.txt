def run(scope, *args)
      inject(Results.new) do |results, callback|
        executed = execute_callback(scope, callback, *args)

        return results.halted! unless continue_execution?(executed)
        results << executed
      end
    end