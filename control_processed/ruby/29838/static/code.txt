def publish_message(opts = {})
      if opts[:MessageBody].nil? || opts[:MessageBody].blank?
        raise Exception.new("publish message parameters invalid")
      else
        Request::Xml.post(message_path) do |request|
          request.content(:Message, opts)
        end
      end
    end