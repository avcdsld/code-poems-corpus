def list_global_by_subscription_for_topic_type_as_lazy(topic_type_name, filter:nil, top:nil, label:nil, custom_headers:nil)
      response = list_global_by_subscription_for_topic_type_async(topic_type_name, filter:filter, top:top, label:label, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_global_by_subscription_for_topic_type_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end