def initialize_copy(other)
      @options = other.options.dup
      @errors = other.errors.dup
      @data, @strings = [], {}
      @entries = Hash.new { |h,k| h.fetch(k.to_s, nil) }

      other.each do |element|
        add element.dup
      end

      self
    end