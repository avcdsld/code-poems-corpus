def hunk_header(hunk)
      old_line, new_line = hunk.first.line_numbers
      old_line ||= 1
      new_line ||= 1

      old_count = hunk.count { |line| [Leg::Line::Removed, Leg::Line::Unchanged].include? line.class }
      new_count = hunk.count { |line| [Leg::Line::Added, Leg::Line::Unchanged].include? line.class }

      old_line = 0 if old_count == 0
      new_line = 0 if new_count == 0

      "@@ -#{old_line},#{old_count} +#{new_line},#{new_count} @@\n"
    end