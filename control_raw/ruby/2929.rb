def redact_sensitive(obj, keys=nil)
      keys ||= %w[
        password passwd pass
        api_key api_token
        access_key secret_key private_key
        secret
        routing_key
        access_token_read access_token_write access_token_path
        webhook_url
        nickserv_password channel_password
        community
        keystore_password truststore_password
        proxy_password
        access_key_id secret_access_key
      ]
      obj = obj.dup
      if obj.is_a?(Hash)
        obj.each do |key, value|
          if keys.include?(key.to_s)
            obj[key] = "REDACTED"
          elsif value.is_a?(Hash) || value.is_a?(Array)
            obj[key] = redact_sensitive(value, keys)
          end
        end
      elsif obj.is_a?(Array)
        obj.map! do |item|
          if item.is_a?(Hash) || item.is_a?(Array)
            redact_sensitive(item, keys)
          else
            item
          end
        end
      end
      obj
    end