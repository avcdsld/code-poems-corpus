def add_provider(provider, *args)
      unless provider.respond_to?(:instance_methods) && provider.instance_methods.include?(:lookup)
        raise ArgumentError, "the given provider does not respond to lookup"
      end

      @provider << provider.new(*args)
    end