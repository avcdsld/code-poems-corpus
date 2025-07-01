def query(query, granularity = nil, t_start = nil, t_end = nil,
              options = {})

      raise ArgumentError unless query.is_a?(String)
      wf_granularity?(granularity)
      raise Wavefront::Exception::InvalidTimestamp if t_start.nil?

      options[:q] = query
      options[:g] = granularity
      options[:s] = parse_time(t_start, true)
      options[:e] = parse_time(t_end, true) if t_end

      options.delete_if { |k, v| v == false && k != :i }
      api.get('api', options)
    end