def table(*columns, &_block)
      rows = []
      yield(rows)

      # determine maximum cell widths
      max_cell_widths = rows.reduce(Array.new(columns.length, 0)) do |result, row|
        lengths = row.map { |column| column.to_s.length }
        result.each_with_index { |length, index| result[index] = ([length, lengths[index]].max rescue length) }
      end
      columns.each_with_index { |col, index| col[:actual_width] ||= max_cell_widths[index] }

      # determine actual column width
      column_widths = columns.map do |column|
        if column[:width] == :rest
          nil
        elsif column[:width]
          column[:width]
        elsif column[:min_width]
          [column[:min_width], column[:actual_width]].max
        elsif column[:max_width]
          [column[:max_width], column[:actual_width]].min
        else
          column[:actual_width]
        end
      end

      if column_widths.include?(nil)
        width_left = options[:width] - ((columns.length - 1) * (style[:cell_separator] ? 3 : 1)) - column_widths.compact.reduce(0) { |sum, col| sum + col }
        column_widths[column_widths.index(nil)] = width_left
      end

      line(:green) if @style[:top_line]

      # Print table header
      if table_has_header?(columns)
        column_titles = []
        columns.each_with_index do |column, index|
          width = column_widths[index]
          alignment = (column[:align] == :right ? '' : '-')
          column_titles.push(colorize("%#{alignment}#{width}s" % column[:title].to_s[0...width], :bold))
        end

        puts column_titles.join(style[:cell_separator] ? " #{characters[:vertical_line]} " : ' ')
        line(:green)
      end

      # Print the rows
      rows.each do |row|
        row_values = []
        columns.each_with_index do |column, index|
          width = column_widths[index]
          case column[:type]
          when :ratio
            if width > 4
              if column[:treshold] && column[:treshold] < row[index].to_f
                bar = ''
                bar << characters[:block] * (width.to_f * column[:treshold]).round
                bar << colorize(characters[:block] * (width.to_f * (row[index].to_f - column[:treshold])).round, :red)
                row_values.push(bar)
              else
                # Create a bar by combining block characters
                row_values.push(characters[:block] * (width.to_f * row[index].to_f).round)
              end
            else
              # Too few characters for a ratio bar. Display nothing
              row_values.push('')
            end
          else
            alignment = (columns[index][:align] == :right ? '' : '-')
            cell_value = "%#{alignment}#{width}s" % row[index].to_s[0...width]
            cell_value = colorize(cell_value, :bold, :brown) if columns[index][:highlight]
            row_values.push(cell_value)
          end
        end
        puts row_values.join(style[:cell_separator] ? " #{characters[:vertical_line]} " : ' ')
      end
    end