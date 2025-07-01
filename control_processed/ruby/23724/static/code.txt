def map_levels
      return [] unless defined?(::Logger::Severity)
      @@map_levels ||=
        ::Logger::Severity.constants.each_with_object([]) do |constant, levels|
          levels[::Logger::Severity.const_get(constant)] = level_by_index_or_error(constant)
        end
    end