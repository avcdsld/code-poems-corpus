def name(gender = :any)
      case gender
      when :any then rand(0..1) == 0 ? name(:male) : name(:female)
      when :male then fetch_sample(MALE_FIRST_NAMES)
      when :female then fetch_sample(FEMALE_FIRST_NAMES)
      else raise ArgumentError, 'Invalid gender, must be one of :any, :male, :female'
      end
    end