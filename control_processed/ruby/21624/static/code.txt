def add_service(key, *args)

      raise ArgumentError.new(
        '#add_service: at least two arguments please'
      ) if args.empty?

      key = key.to_s
      path, klass, opts = args

      key = "s_#{key}" unless SERVICE_PREFIX.match(key)

      aa = [ self, opts ].compact

      service = if klass

        require(path)

        @services[key] = Ruote.constantize(klass).new(*aa)

      elsif path.is_a?(Class)

        @services[key] = path.new(*aa)

      else

        @services[key] = path
      end

      (class << self; self; end).class_eval(
        %{ def #{key[2..-1]}; @services['#{key}']; end })
          #
          # This 'two-liner' will add an instance method to Context for this
          # service.
          #
          # If the service key is 's_dishwasher', then the service will be
          # available via Context#dishwasher.
          #
          # I.e. dishwasher = engine.context.dishwasher

      service
    end