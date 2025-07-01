def perform_request
      @raw_response = Braintree::CreditCard.update(@options[:token], whitelist_options)
      Conduit::Driver::Braintree::Json::CreditCard.new(@raw_response).to_json
    end