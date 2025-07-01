def on_slim_output(escape, code, content)
      code = code + ' do' unless code =~ BLOCK_REGEX || empty_exp?(content)
      [:slim, :output, escape, code, compile(content)]
    end