def append_new_context(klass, *args)
      klass.new(*args).tap do |new_context|
        new_context.register_with_parent(current_context)
      end
    end