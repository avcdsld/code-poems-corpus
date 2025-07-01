def call(entry)
      lines = entry.message.strip.split(Lumberjack::LINE_SEPARATOR)
      formatted_time = format_time(entry.time) if @template_include_time
      message = @first_line_template % [formatted_time, entry.severity_label, entry.progname, entry.pid, entry.unit_of_work_id, lines.shift]
      lines.each do |line|
        message << @additional_line_template % [formatted_time, entry.severity_label, entry.progname, entry.pid, entry.unit_of_work_id, line]
      end
      message
    end