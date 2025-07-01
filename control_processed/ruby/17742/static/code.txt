def msearch(body=[])
      raise ArgumentError, "msearch takes an array!" unless body.is_a?(Array)
      fmt_body = body.map {|l| MultiJson.dump(l) }.join("\n") << "\n"

      res = request(:get, path_uri("/_msearch"), {}, fmt_body, {}, :mashify => false)

      errors = res['responses'].map { |response| response['error'] }.compact
      if !errors.empty?
        raise RequestError.new(res), "Could not msearch #{errors.inspect}"
      end

      res['responses'].map {|r| SearchResults.new(r)}
    end