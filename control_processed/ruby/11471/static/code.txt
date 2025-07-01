def report(output)
      output.title(title)

      if total_requests == 0
        output << "None found.\n"
        return
      end

      days = [1, timespan].max
      output.table({}, { align: :right }, { type: :ratio, width: :rest, treshold: 0.15 }) do |rows|
        @hour_frequencies.each_with_index do |requests, index|
          ratio            = requests.to_f / total_requests.to_f
          requests_per_day = (requests / days).ceil
          rows << ["#{index.to_s.rjust(3)}:00", '%d hits/day' % requests_per_day, ratio]
        end
      end
    end