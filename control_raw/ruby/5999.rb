def list_certificates(resource_group_name, certificate_order_name, custom_headers:nil)
      first_page = list_certificates_as_lazy(resource_group_name, certificate_order_name, custom_headers:custom_headers)
      first_page.get_all_items
    end