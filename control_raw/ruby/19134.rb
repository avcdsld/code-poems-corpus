def format_source_file_line(source_file, line_number)
      return '' if source_file.nil? || source_file.empty?
      filename = if compilation_dir && source_file.start_with?(compilation_dir)
        stripped_file = source_file[compilation_dir.length..-1]
        stripped_file.start_with?('/') ? stripped_file[1..-1] : stripped_file
      else
        source_file
      end
      "(#{filename.sub(%r{^environments/production/}, '')}:#{line_number})"
    end