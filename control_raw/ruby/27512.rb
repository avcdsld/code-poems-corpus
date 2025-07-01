def process_response(response)
        raise ArgumentError, 'response is null' if response.nil?

        if block_given?
          yield
        end


        # return code
        if 401 == response.code
          raise UnauthorizedError, compose_error_message(response)
        elsif 500 == response.code
          raise ServerError, compose_error_message(response)
        elsif 2 != (response.code / 100)
          raise OrientdbError, "unexpected return code, code=#{response.code}, body=#{compose_error_message(response)}"
        end

        content_type = response.headers[:content_type] if connection_library == :restclient
        content_type = response.headers['Content-Type'] if connection_library == :excon
        content_type ||= 'text/plain'

        rslt = case
          when content_type.start_with?('text/plain')
            response.body
          when content_type.start_with?('application/x-gzip')
            response.body
          when content_type.start_with?('application/json')
            ::JSON.parse(response.body)
          else
            raise OrientdbError, "unsuported content type: #{content_type}"
          end

        rslt
      end