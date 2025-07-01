def write_url_range(*args)
    # Check for a cell reference in A1 notation and substitute row and column
    args = row_col_notation(args)

    # Check the number of args
    return -1 if args.size < 5

    # Reverse the order of _string_ and _format_ if necessary. We work on a copy
    # in order to protect the callers args.
    #
    args[5], args[6] = [ args[6], args[5] ] if args[5].respond_to?(:xf_index)

    url = args[4]

    # Check for internal/external sheet links or default to web link
    return write_url_internal(*args) if url =~ /^internal:/
    return write_url_external(*args) if url =~ /^external:/
    write_url_web(*args)
  end