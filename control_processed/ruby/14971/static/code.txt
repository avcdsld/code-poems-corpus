def emit_eof_comments
      emit_eol_comments
      comments_left = comments.take_all
      return if comments_left.empty?

      buffer.nl
      emit_comments(comments_left)
    end