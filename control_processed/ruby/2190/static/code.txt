def check_commas_after_args(args, arg_type)
      # For each arg except the last, check the character following the comma
      args[0..-2].each do |arg|
        # Sometimes the line we're looking at doesn't even contain a comma!
        next unless engine.lines[arg.line - 1].include?(',')

        comma_position = find_comma_position(arg)

        # Check for space or newline after comma (we allow arguments to be split
        # up over multiple lines).
        spaces = 0
        while (char = character_at(comma_position, spaces + 1)) == ' '
          spaces += 1
        end
        next if char == "\n" || # Ignore trailing spaces
                valid_spaces_after_comma?(spaces)

        style_message = config['style'].tr('_', ' ')
        add_lint comma_position, "Commas in #{arg_type} should be followed by #{style_message}"
      end
    end