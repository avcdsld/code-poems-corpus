def list_site_detectors_slot(resource_group_name, site_name, diagnostic_category, slot, custom_headers:nil)
      first_page = list_site_detectors_slot_as_lazy(resource_group_name, site_name, diagnostic_category, slot, custom_headers:custom_headers)
      first_page.get_all_items
    end