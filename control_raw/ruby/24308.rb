def ratiometric
      ptr = ::FFI::MemoryPointer.new(:int)
      Klass.getRatiometric(@handle, ptr)
      (ptr.get_int(0) == 0) ? false : true
    end