def extract_body( params )
      body = params.delete :body
      return if body.nil?

      body =
        case body
        when String
          body
        when Array
          body << nil unless body.last.nil?
          body.join "\n"
        else
          MultiJson.dump body
        end

      # Prevent excon from changing the encoding (see https://github.com/github/elastomer-client/issues/138)
      body.freeze
    end