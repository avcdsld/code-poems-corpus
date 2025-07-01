def succeeded(topic, event)
      subscribers_for(topic).each{ |subscriber| subscriber.succeeded(event) }
    end