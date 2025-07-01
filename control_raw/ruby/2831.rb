def minify_source_list(directive, source_list)
      source_list = source_list.compact
      if source_list.include?(STAR)
        keep_wildcard_sources(source_list)
      else
        source_list = populate_nonces(directive, source_list)
        source_list = reject_all_values_if_none(source_list)

        unless directive == REPORT_URI || @preserve_schemes
          source_list = strip_source_schemes(source_list)
        end
        dedup_source_list(source_list)
      end
    end