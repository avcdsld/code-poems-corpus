def get_line(exception)
      # SyntaxErrors have weird line reporting
      # when there's trailing whitespace
      if exception.is_a?(::SyntaxError)
        return (exception.message.scan(/:(\d+)/).first || ["??"]).first
      end
      (exception.backtrace[0].scan(/:(\d+)/).first || ["??"]).first
    end