def method_missing(meth, *args, &block)
      if !loaded?
        self.loaded = true
        reload
        send(meth, *args, &block)
      else
        super
      end
    end