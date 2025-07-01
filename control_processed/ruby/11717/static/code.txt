def get(key, options = {}, not_found = :reject, found = :return)
      key_subst = if key.start_with? '/'
                    key[1..-1]
                  else
                    key.freeze
                  end
      @key = key_subst
      @options = options
      custom_params = []
      custom_params << recurse_get(@options)
      custom_params << use_consistency(options)
      custom_params << dc(@options)
      custom_params << keys(@options)
      custom_params << separator(@options)

      return_nil_values = @options && @options[:nil_values]
      transformation = @options && @options[:transformation] && @options[:transformation].methods.find_index(:call) ? @options[:transformation] : nil

      raw = send_get_request(@conn_no_err, ["/v1/kv/#{@key}"], options, custom_params)
      if raw.status == 404
        case not_found
        when :reject
          raise Diplomat::KeyNotFound, key
        when :return
          return @value = ''
        when :wait
          index = raw.headers['x-consul-index']
        end
      elsif raw.status == 200
        case found
        when :reject
          raise Diplomat::KeyAlreadyExists, key
        when :return
          @raw = raw
          @raw = parse_body
          return @raw.first['ModifyIndex'] if @options && @options[:modify_index]
          return @raw.first['Session'] if @options && @options[:session]
          return decode_values if @options && @options[:decode_values]
          return convert_to_hash(return_value(return_nil_values, transformation, true)) if @options && @options[:convert_to_hash]

          return return_value(return_nil_values, transformation)
        when :wait
          index = raw.headers['x-consul-index']
        end
      else
        raise Diplomat::UnknownStatus, "status #{raw.status}: #{raw.body}"
      end

      # Wait for first/next value
      custom_params << use_named_parameter('index', index)
      if options.nil?
        options = { timeout: 86_400 }
      else
        options[:timeout] = 86_400
      end
      @raw = send_get_request(@conn, ["/v1/kv/#{@key}"], options, custom_params)
      @raw = parse_body
      return_value(return_nil_values, transformation)
    end