def []=(*args)
      vector = args.pop
      axis = extract_axis(args)
      names = args

      dispatch_to_axis axis, :insert_or_modify, names, vector
    end