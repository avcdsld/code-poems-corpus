def wf_webhook_id?(id)
      return true if id.is_a?(String) && id =~ /^[a-zA-Z0-9]{16}$/
      raise Wavefront::Exception::InvalidWebhookId
    end