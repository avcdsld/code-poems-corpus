def format(arg)
      if arg.is_a?(Exception)
        "#{arg.class}: #{arg.message}\n\t" <<
        arg.backtrace.join("\n\t") << "\n"
      elsif arg.respond_to?(:to_str)
        arg.to_str
      else
        arg.inspect
      end
    end