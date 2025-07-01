def local_number
      return national unless possible?
      format_match, format_string = formatting_data

      if format_string =~ /^.*[0-9]+.*\$1/ && format_match
        format_string.gsub(/^.*\$2/, '$2')
          .gsub(/\$\d/) { |el| format_match[el[1].to_i] }
      else
        national
      end
    end