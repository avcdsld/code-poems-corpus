def list_geo_regions_as_lazy_with_http_info(sku:nil, linux_workers_enabled:nil, custom_headers:nil)
      list_geo_regions_as_lazy_async(sku:sku, linux_workers_enabled:linux_workers_enabled, custom_headers:custom_headers).value!
    end