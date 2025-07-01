def store_defrow   #:nodoc:
    record   = 0x0225      # Record identifier
    length   = 0x0004      # Number of bytes to follow

    grbit    = 0x0000      # Options.
    height   = 0x00FF      # Default row height

    header = [record, length].pack("vv")
    data   = [grbit,  height].pack("vv")

    prepend(header, data)
  end