def call_function_with_scope(scope, function_name, *args, &block)
      internal_call_function(scope, function_name, args, &block)
    end