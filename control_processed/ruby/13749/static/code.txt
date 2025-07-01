def parse_backtrace(backtrace)
      Backtrace.parse(
        backtrace,
        filters: construct_backtrace_filters(opts),
        config: config,
        source_radius: config[:'exceptions.source_radius']
      ).to_a
    end