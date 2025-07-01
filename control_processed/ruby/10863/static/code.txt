def list(resource_uri, timespan:nil, interval:nil, metricnames:nil, aggregation:nil, top:nil, orderby:nil, filter:nil, result_type:nil, metricnamespace:nil, custom_headers:nil)
      response = list_async(resource_uri, timespan:timespan, interval:interval, metricnames:metricnames, aggregation:aggregation, top:top, orderby:orderby, filter:filter, result_type:result_type, metricnamespace:metricnamespace, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end