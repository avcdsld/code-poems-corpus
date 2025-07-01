def report_table(output, sort, options = {}, &_block)
      output.puts
      top_categories = output.slice_results(sorted_by(sort))
      output.with_style(top_line: true) do
        output.table(*statistics_header(title: options[:title], highlight: sort)) do |rows|
          top_categories.each { |(category, _)| rows << statistics_row(category) }
        end
      end
    end