def set_value(value,format=CFDate::TIMESTAMP_UNIX)
      if(format == CFDate::TIMESTAMP_UNIX) then
        @value = Time.at(value)
      else
        @value = Time.at(value + CFDate::DATE_DIFF_APPLE_UNIX)
      end
    end