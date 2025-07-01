def source_regex
      return @source_regex if defined? @source_regex
      return unless meta.source

      source = meta.source.dup.sub(/\A#{SOURCE_PREFIX}/, '')
      source = source.sub(/#{SOURCE_SUFFIX}\z/, '')

      escaped_source = Regexp.escape(source)
      @source_regex = /#{SOURCE_PREFIX}#{escaped_source}(?:#{SOURCE_SUFFIX})?/i
    end