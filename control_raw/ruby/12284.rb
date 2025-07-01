def frequencies type=:count
      counts = @cat_hash.values.map(&:size)
      values =
        case type
        when :count
          counts
        when :fraction
          counts.map { |c| c / size.to_f }
        when :percentage
          counts.map { |c| c / size.to_f * 100 }
        else
          raise ArgumentError, 'Type should be either :count, :fraction or'\
          " :percentage. #{type} not supported."
        end
      Daru::Vector.new values, index: categories, name: name
    end