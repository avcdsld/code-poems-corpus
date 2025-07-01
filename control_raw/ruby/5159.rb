def connection
      @connection ||= Faraday.new(faraday_options) do |builder|
        builder.use Faraday::Request::UrlEncoded
        builder.use Restforce::Middleware::Mashify, nil, @options
        builder.response :json

        if Restforce.log?
          builder.use Restforce::Middleware::Logger,
                      Restforce.configuration.logger,
                      @options
        end

        builder.adapter @options[:adapter]
      end
    end