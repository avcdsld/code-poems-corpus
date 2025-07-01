def filter_rows
      return to_enum(:filter_rows) unless block_given?

      keep_rows = @index.map { |index| yield access_row(index) }

      where keep_rows
    end