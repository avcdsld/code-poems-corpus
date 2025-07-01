def read_from_string(buf)
      @lexer.stream_stash([FileIO.new(StringIO.new(buf), "-")])
      parse.each do |toplevel_ast|
        @gen.emit_toplevel(toplevel_ast)
      end
      @lexer.stream_unstash
    end