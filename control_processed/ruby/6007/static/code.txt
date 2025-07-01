def reissue(resource_group_name, certificate_order_name, reissue_certificate_order_request, custom_headers:nil)
      response = reissue_async(resource_group_name, certificate_order_name, reissue_certificate_order_request, custom_headers:custom_headers).value!
      nil
    end