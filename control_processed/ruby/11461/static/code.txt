def report(output)
      output.title(options[:title]) if options[:title]

      if @last > 0 && @first < 99_999_999_999_999
        output.with_style(cell_separator: false) do
          output.table({ width: 20 }, {}) do |rows|
            rows << ['First request:', first_timestamp.strftime('%Y-%m-%d %H:%M:%I')]
            rows << ['Last request:',  last_timestamp.strftime('%Y-%m-%d %H:%M:%I')]
            rows << ['Total time analyzed:', "#{timespan.ceil} days"]
          end
        end
      end
    end