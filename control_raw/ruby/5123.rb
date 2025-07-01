def debug(*messages)
      longest = messages.max_by(&:length).size
      width = TTY::Screen.width - longest
      print cursor.save
      messages.each_with_index do |msg, i|
        print cursor.move_to(width, i)
        print cursor.clear_line_after
        print msg
      end
      print cursor.restore
    end