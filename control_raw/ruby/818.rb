def parse(source, options = {})
      @options = options
      @profiling = options[:profile]
      @line_numbers = options[:line_numbers] || @profiling
      parse_context = options.is_a?(ParseContext) ? options : ParseContext.new(options)
      @root = Document.parse(tokenize(source), parse_context)
      @warnings = parse_context.warnings
      self
    end