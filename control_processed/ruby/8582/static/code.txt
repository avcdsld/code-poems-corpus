def update(fabric_name, v_center_name, update_vcenter_request, custom_headers:nil)
      response = update_async(fabric_name, v_center_name, update_vcenter_request, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end