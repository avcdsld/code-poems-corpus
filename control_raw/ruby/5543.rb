def perform(action, options = {})
      return unless %i[
        backtrace
        down
        finish
        frame
        next
        step
        up
      ].include?(action)

      send("perform_#{action}", options)
    end