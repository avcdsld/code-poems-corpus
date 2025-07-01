def read_line(frame)
      file, line_number = frame.split(/:/, 2)
      line_number = line_number.to_i
      lines = File.readlines(file)

      lines[line_number - 1]
    end