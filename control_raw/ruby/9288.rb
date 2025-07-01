def create_lab(resource_group_name, lab_account_name, create_lab_properties, custom_headers:nil)
      response = create_lab_async(resource_group_name, lab_account_name, create_lab_properties, custom_headers:custom_headers).value!
      nil
    end