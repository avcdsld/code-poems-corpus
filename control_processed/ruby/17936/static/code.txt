def refund(
      amazon_capture_id,
      refund_reference_id,
      amount,
      currency_code: @currency_code,
      seller_refund_note: nil,
      soft_descriptor: nil,
      provider_credit_reversal_details: nil,
      merchant_id: @merchant_id,
      mws_auth_token: nil
    )

      parameters = {
        'Action' => 'Refund',
        'SellerId' => merchant_id,
        'AmazonCaptureId' => amazon_capture_id,
        'RefundReferenceId' => refund_reference_id,
        'RefundAmount.Amount' => amount,
        'RefundAmount.CurrencyCode' => currency_code
      }

      optional = {
        'SellerRefundNote' => seller_refund_note,
        'SoftDescriptor' => soft_descriptor,
        'MWSAuthToken' => mws_auth_token
      }

      optional.merge!(set_provider_credit_reversal_details(provider_credit_reversal_details)) if provider_credit_reversal_details

      operation(parameters, optional)
    end