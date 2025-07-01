def weeks_for_month(year, month_param)
      merch_month = get_merch_month_param(month_param)

      start_date = start_of_month(year, merch_month)

      weeks = (end_of_month(year, merch_month) - start_date + 1) / 7

      (1..weeks).map do |week_num|
        week_start = start_date + ((week_num - 1) * 7)
        week_end = week_start + 6

        MerchWeek.new(week_start, { 
          start_of_week: week_start, 
          end_of_week: week_end, 
          week: week_num, 
          calendar: RetailCalendar.new
        })
      end
    end