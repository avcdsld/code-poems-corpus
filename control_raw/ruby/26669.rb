def get_z(idx)
      check_bounds(idx)
      double_ptr = FFI::MemoryPointer.new(:double)
      FFIGeos.GEOSCoordSeq_getZ_r(Geos.current_handle_pointer, ptr, idx, double_ptr)
      double_ptr.read_double
    end