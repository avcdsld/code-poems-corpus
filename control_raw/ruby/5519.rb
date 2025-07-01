def set_working_days(working_days)
      @working_days = (working_days || default_working_days).map do |day|
        day.downcase.strip[0..2].tap do |normalised_day|
          raise "Invalid day #{day}" unless DAY_NAMES.include?(normalised_day)
        end
      end
      extra_working_dates_names = @extra_working_dates.map { |d| d.strftime("%a").downcase }
      return if (extra_working_dates_names & @working_days).none?
      raise ArgumentError, 'Extra working dates cannot be on working days'
    end