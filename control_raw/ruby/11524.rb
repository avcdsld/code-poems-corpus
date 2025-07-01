def add(*args)
      args.flatten! # allow [] as a param
      args = args.collect(&:to_sym)

      # make the columns inheritable
      @_inheritable.concat(args)
      # then add columns to @set (unless they already exist)
      args.each { |a| @set << ActiveScaffold::DataStructures::Column.new(a.to_sym, @active_record_class) unless find_by_name(a) }
    end