def call(request_env)
      request_body = request_env[:body]

      begin
        request_env[:body] = request_body

        @app.call(request_env).on_complete do |response_env|
          status_code = response_env.status

          if @times > 0 && (status_code == 408 || (status_code >= 500 && status_code != 501 && status_code != 505))
            sleep @delay
            fail 'faraday_retry'
          end
        end
      rescue Exception => e
        raise e if e.message != 'faraday_retry'
        @times = @times - 1
        retry
      end
    end