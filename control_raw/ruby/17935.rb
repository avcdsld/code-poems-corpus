def get_capture_details(
      amazon_capture_id,
      merchant_id: @merchant_id,
      mws_auth_token: nil
    )

      parameters = {
        'Action' => 'GetCaptureDetails',
        'SellerId' => merchant_id,
        'AmazonCaptureId' => amazon_capture_id
      }

      optional = {
        'MWSAuthToken' => mws_auth_token
      }

      operation(parameters, optional)
    end