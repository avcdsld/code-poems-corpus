def parse_params(params)
      args = params.split(/\s+/).map(&:strip)
      invalid_args!(args) unless args.any?

      if args[0].to_s == OEMBED_ARG # TODO: remove after deprecation cycle
        arguments_deprecation_warning(args)
        args.shift
      end

      url, *api_args = args
      ApiRequest.new(url, parse_args(api_args))
    end