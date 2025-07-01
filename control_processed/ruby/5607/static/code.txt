def set!(date)
      date = Date.parse date if date.is_a?(String)

      message = "DateField##{__callee__} only accepts instances of Date or Time"
      raise ArgumentError, message unless [Date, ::Time].include?(date.class)

      date_string = date.strftime('%Y-%m-%d')
      element_call(:wait_for_writable) { execute_js(:setValue, @element, date_string) }
    end