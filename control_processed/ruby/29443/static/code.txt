def itrp_upload(itrp, key_template, key, attachment)
      uri = itrp[:upload_uri] =~ /\/v1/ ? itrp[:upload_uri] : itrp[:upload_uri].gsub('/attachments', '/v1/attachments')
      response = send_file(uri, {file: attachment, key: key_template}, @client.send(:expand_header))
      raise "ITRP upload to #{itrp[:upload_uri]} for #{key} failed: #{response.message}" unless response.valid?
    end