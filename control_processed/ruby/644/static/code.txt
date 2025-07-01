def write_json_integer(num)
      @context.write(trans)
      escapeNum = @context.escapeNum
      if (escapeNum)
        trans.write(@@kJSONStringDelimiter)
      end
      trans.write(num.to_s);
      if (escapeNum)
        trans.write(@@kJSONStringDelimiter)
      end
    end