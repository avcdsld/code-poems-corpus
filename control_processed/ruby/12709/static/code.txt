def sass_backtrace_str(default_filename = "an unknown file")
      lines = message.split("\n")
      msg = lines[0] + lines[1..-1].
        map {|l| "\n" + (" " * "Error: ".size) + l}.join
      "Error: #{msg}" +
        sass_backtrace.each_with_index.map do |entry, i|
          "\n        #{i == 0 ? 'on' : 'from'} line #{entry[:line]}" +
            " of #{entry[:filename] || default_filename}" +
            (entry[:mixin] ? ", in `#{entry[:mixin]}'" : "")
        end.join
    end