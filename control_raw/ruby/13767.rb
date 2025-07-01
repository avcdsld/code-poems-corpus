def marc_instrument_codes_normalized(spec = "048")
      soloist_suffix = ".s"

      extractor = MarcExtractor.new("048", :separator => nil)

      return lambda do |record, accumulator|
        accumulator.concat(
          extractor.collect_matching_lines(record) do |field, spec, extractor|
            values = []

            field.subfields.each do |sf|
              v = sf.value
              # Unless there's at least two chars, it's malformed, we can
              # do nothing
              next unless v.length >= 2

              # Index both with and without number -- both with soloist suffix
              # if in a $b
              values << v
              values << "#{v}#{soloist_suffix}" if sf.code == 'b'
              if v.length >= 4
                bare = v.slice(0,2) # just the prefix
                values << bare
                values << "#{bare}#{soloist_suffix}" if sf.code == 'b'
              end
            end
            values
          end.uniq
        )
      end
    end