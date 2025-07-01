def chunk_to_lines chunk, state, start, depth, parent=nil, color=nil, star_color=nil
    prefix = " " * @indent_spaces * depth
    case chunk
    when :fake_root
      [[[:missing_message_color, "#{prefix}<one or more unreceived messages>"]]]
    when nil
      [[[:missing_message_color, "#{prefix}<an unreceived message>"]]]
    when Message
      message_patina_lines(chunk, state, start, parent, prefix, color, star_color) +
        (chunk.is_draft? ? [[[:draft_notification_color, prefix + " >>> This message is a draft. Hit 'e' to edit, 'y' to send. <<<"]]] : [])

    else
      raise "Bad chunk: #{chunk.inspect}" unless chunk.respond_to?(:inlineable?) ## debugging
      if chunk.inlineable?
        lines = maybe_wrap_text(chunk.lines)
        lines.map { |line| [[chunk.color, "#{prefix}#{line}"]] }
      elsif chunk.expandable?
        case state
        when :closed
          [[[chunk.patina_color, "#{prefix}+ #{chunk.patina_text}"]]]
        when :open
          lines = maybe_wrap_text(chunk.lines)
          [[[chunk.patina_color, "#{prefix}- #{chunk.patina_text}"]]] + lines.map { |line| [[chunk.color, "#{prefix}#{line}"]] }
        end
      else
        [[[chunk.patina_color, "#{prefix}x #{chunk.patina_text}"]]]
      end
    end
  end