def add_stdout(*args)
      args = args.flatten.compact
      args = args.first.split($/) if args.size == 1
      self << args
      self.flatten!
    end