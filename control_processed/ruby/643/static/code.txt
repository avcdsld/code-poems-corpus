def write_json_base64(str)
      @context.write(trans)
      trans.write(@@kJSONStringDelimiter)
      trans.write(Base64.strict_encode64(str))
      trans.write(@@kJSONStringDelimiter)
    end