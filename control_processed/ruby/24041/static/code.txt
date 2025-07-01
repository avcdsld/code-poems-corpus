def unify(field, pattern, value = nil)
      pattern = Regexp.new(pattern) unless pattern.is_a?(Regexp)

      block = if block_given?
        Proc.new
      else
        Proc.new { |e| e[field] = value }
      end

      each_entry do |entry|
        if entry.field?(field) && entry[field].to_s =~ pattern
          block.call(entry)
        end
      end

      self
    end