def collect_matching_lines(marc_record)
      results = []
      self.each_matching_line(marc_record) do |field, spec, extractor|
        results.concat [yield(field, spec, extractor)].flatten
      end
      return results
    end