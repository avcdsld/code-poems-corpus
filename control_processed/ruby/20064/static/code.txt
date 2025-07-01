def calculate_spans #:nodoc:
      span_min = nil
      span_max = 0
      spans = []

      (@dim_rowmin .. @dim_rowmax).each do |row_num|
        if @cell_data_table[row_num]
          span_min, span_max = calc_spans(@cell_data_table, row_num, span_min, span_max)
        end

        # Calculate spans for comments.
        if @comments[row_num]
          span_min, span_max = calc_spans(@comments, row_num, span_min, span_max)
        end

        if ((row_num + 1) % 16 == 0) || (row_num == @dim_rowmax)
          span_index = row_num / 16
          if span_min
            span_min += 1
            span_max += 1
            spans[span_index] = "#{span_min}:#{span_max}"
            span_min = nil
          end
        end
      end

      @row_spans = spans
    end