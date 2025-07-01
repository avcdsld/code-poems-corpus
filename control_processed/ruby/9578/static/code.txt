def to_json(*a)
      {exception_message: exception_message, message: @msg,  stacktrace: exception_stacktrace, result: result}.to_json(*a)
    end