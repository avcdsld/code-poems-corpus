def verify
      params = to_hash.downcase_keys
      if TaxCloud.configuration.usps_username
        params = params.merge(
          'uspsUserID' => TaxCloud.configuration.usps_username
        )
      end
      response = TaxCloud.client.request(:verify_address, params)
      TaxCloud::Responses::VerifyAddress.parse(response)
    end