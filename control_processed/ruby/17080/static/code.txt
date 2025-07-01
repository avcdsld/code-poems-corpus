def connection
      @connection ||= Faraday.new(faraday_client_options) do |connection|
        connection.request :json
        connection.response :json
        connection.adapter Faraday.default_adapter
      end
    end