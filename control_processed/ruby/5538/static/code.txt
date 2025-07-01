def send_http_request
      net_http_options = [uri.host, uri.port, use_ssl: true]
      ActiveSupport::Notifications.instrument 'request.yt' do |payload|
        payload[:method] = @method
        payload[:request_uri] = uri
        payload[:response] = Net::HTTP.start(*net_http_options) do |http|
          http.request http_request
        end
      end
    end