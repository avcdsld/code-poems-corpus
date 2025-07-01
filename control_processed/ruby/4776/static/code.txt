def all(query)
      return to_enum(:all, query) unless block_given?

      if @hash.include? query
        yield @hash[query]
        return
      end

      case query
      when String
        optimize_if_necessary!

        # see if any of the regexps match the string
        @regexes.each do |regex|
          match = regex.match(query)
          next unless match
          @regex_counts[regex] += 1
          value = @hash[regex]
          if value.respond_to? :call
            yield value.call(match)
          else
            yield value
          end
        end

      when Numeric
        # see if any of the ranges match the integer
        @ranges.each do |range|
          yield @hash[range] if range.cover? query
        end

      when Regexp
        # Reverse operation: `rash[/regexp/]` returns all the hash's string keys which match the regexp
        @hash.each do |key, val|
          yield val if key.is_a?(String) && query =~ key
        end
      end
    end