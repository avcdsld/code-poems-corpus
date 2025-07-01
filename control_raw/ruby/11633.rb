def transform(success, failure)
      promise = Promise.new(@options)
      on_complete_match do |m|
        m.success { |value| promise.success(success.call(value)) }
        m.failure { |error| promise.failure(failure.call(error)) }
      end
      promise.to_future
    end