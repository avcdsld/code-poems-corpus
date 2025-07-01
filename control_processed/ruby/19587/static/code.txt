def pack_doper(operator, token)   #:nodoc:
    doper       = ''
    string      = ''

    # Return default doper for non-defined filters.
    unless operator
      return pack_unused_doper, string
    end

    if token.to_s =~ /^blanks|nonblanks$/i
      doper  = pack_blanks_doper(operator, token)
    elsif operator == 2 or
      !(token.to_s  =~ /^([+-]?)(?=\d|\.\d)\d*(\.\d*)?([Ee]([+-]?\d+))?$/)
      # Excel treats all tokens as strings if the operator is equality, =.
      string = token.to_s
      ruby_19 { string = convert_to_ascii_if_ascii(string) }

      encoding = 0
      length   = string.bytesize

      # Handle utf8 strings
      if is_utf8?(string)
        string = utf8_to_16be(string)
        encodign = 1
      end

      string =
        ruby_18 { [encoding].pack('C') +  string } ||
        ruby_19 { [encoding].pack('C') +  string.force_encoding('BINARY') }
      doper  = pack_string_doper(operator, length)
    else
      string = ''
      doper  = pack_number_doper(operator, token)
    end

    [doper, string]
  end