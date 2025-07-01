def tokenize string
      return nil if string.empty?
      return string if @string_cache.key?(string)
      return @symbol_cache[string] if @symbol_cache.key?(string)

      case string
      # Check for a String type, being careful not to get caught by hash keys, hex values, and
      # special floats (e.g., -.inf).
      when /^[^\d\.:-]?[A-Za-z_\s!@#\$%\^&\*\(\)\{\}\<\>\|\/\\~;=]+/, /\n/
        if string.length > 5
          @string_cache[string] = true
          return string
        end

        case string
        when /^[^ytonf~]/i
          @string_cache[string] = true
          string
        when '~', /^null$/i
          nil
        when /^(yes|true|on)$/i
          true
        when /^(no|false|off)$/i
          false
        else
          @string_cache[string] = true
          string
        end
      when TIME
        begin
          parse_time string
        rescue ArgumentError
          string
        end
      when /^\d{4}-(?:1[012]|0\d|\d)-(?:[12]\d|3[01]|0\d|\d)$/
        require 'date'
        begin
          class_loader.date.strptime(string, '%Y-%m-%d')
        rescue ArgumentError
          string
        end
      when /^\.inf$/i
        Float::INFINITY
      when /^-\.inf$/i
        -Float::INFINITY
      when /^\.nan$/i
        Float::NAN
      when /^:./
        if string =~ /^:(["'])(.*)\1/
          @symbol_cache[string] = class_loader.symbolize($2.sub(/^:/, ''))
        else
          @symbol_cache[string] = class_loader.symbolize(string.sub(/^:/, ''))
        end
      when /^[-+]?[0-9][0-9_]*(:[0-5]?[0-9]){1,2}$/
        i = 0
        string.split(':').each_with_index do |n,e|
          i += (n.to_i * 60 ** (e - 2).abs)
        end
        i
      when /^[-+]?[0-9][0-9_]*(:[0-5]?[0-9]){1,2}\.[0-9_]*$/
        i = 0
        string.split(':').each_with_index do |n,e|
          i += (n.to_f * 60 ** (e - 2).abs)
        end
        i
      when FLOAT
        if string =~ /\A[-+]?\.\Z/
          @string_cache[string] = true
          string
        else
          Float(string.gsub(/[,_]|\.([Ee]|$)/, '\1'))
        end
      else
        int = parse_int string.gsub(/[,_]/, '')
        return int if int

        @string_cache[string] = true
        string
      end
    end