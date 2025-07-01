def dist(*args)
      case args.length
      when 4
        return dist2d(*args)
      when 6
        return dist3d(*args)
      else
        raise ArgumentError, 'takes 4 or 6 parameters'
      end
    end