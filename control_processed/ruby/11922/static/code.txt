def unsubscribe_subscription_url_for(subscription, params = {})
      options = params.dup
      options.delete(:devise_default_routes) ?
        send("unsubscribe_#{routing_scope(options)}subscription_url", subscription, options) :
        send("unsubscribe_#{routing_scope(options)}#{subscription.target.to_resource_name}_subscription_url", subscription.target, subscription, options)
    end