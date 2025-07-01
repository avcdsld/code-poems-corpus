def get_row(row)
      row = @row_keys[row]
      row.nil? ? nil : @col_keys.map { |c, ci| [c, @content[row][ci]] }.to_h
    end