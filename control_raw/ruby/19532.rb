def write_row(*args)
    # Check for a cell reference in A1 notation and substitute row and column
    args = row_col_notation(args)

    # Catch non array refs passed by user.
    raise "Not an array ref in call to write_row() #{$!}" unless args[2].respond_to?(:to_ary)

    row, col, tokens, options = args
    error = false
    if tokens
      tokens.each do |token|
        # Check for nested arrays
        if token.respond_to?(:to_ary)
          ret = write_col(row, col, token, options)
        else
          ret = write(row, col, token, options)
        end

        # Return only the first error encountered, if any.
        error ||= ret
        col += 1
      end
    end
    error || 0
  end