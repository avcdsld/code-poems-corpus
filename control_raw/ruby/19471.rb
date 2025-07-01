def store_axcext  # :nodoc:
    record       = 0x1062     # Record identifier.
    length       = 0x0012     # Number of bytes to follow.
    catMin       = 0x0000     # Minimum category on axis.
    catMax       = 0x0000     # Maximum category on axis.
    catMajor     = 0x0001     # Value of major unit.
    unitMajor    = 0x0000     # Units of major unit.
    catMinor     = 0x0001     # Value of minor unit.
    unitMinor    = 0x0000     # Units of minor unit.
    unitBase     = 0x0000     # Base unit of axis.
    catCrossDate = 0x0000     # Crossing point.
    grbit        = 0x00EF     # Option flags.

    store_simple(record, length, catMin, catMax, catMajor, unitMajor,
                 catMinor, unitMinor, unitBase, catCrossDate, grbit)
  end