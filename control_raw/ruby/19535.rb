def write_url(*args)
    # Check for a cell reference in A1 notation and substitute row and column
    args = row_col_notation(args)

    # Check the number of args
    return -1 if args.size < 3

    # Add start row and col to arg list
    write_url_range(args[0], args[1], *args)
  end