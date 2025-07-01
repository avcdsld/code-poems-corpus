def scoreboard
      @pending_examples ||= []
      @failed_examples ||= []
      padding = @example_count.to_s.length
      [ @current.to_s.rjust(padding),
        success_color((@current - @pending_examples.size - @failed_examples.size).to_s.rjust(padding)),
        pending_color(@pending_examples.size.to_s.rjust(padding)),
        failure_color(@failed_examples.size.to_s.rjust(padding)) ]
    end