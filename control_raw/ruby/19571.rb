def store_externsheet(sheetname)   #:nodoc:
    record    = 0x0017         # Record identifier
    # length;                     # Number of bytes to follow

    # cch                        # Length of sheet name
    # rgch                       # Filename encoding

    # References to the current sheet are encoded differently to references to
    # external sheets.
    #
    if @name == sheetname
      sheetname = ''
      length    = 0x02  # The following 2 bytes
      cch       = 1     # The following byte
      rgch      = 0x02  # Self reference
    else
      length    = 0x02 + sheetname.bytesize
      cch       = sheetname.bytesize
      rgch      = 0x03  # Reference to a sheet in the current workbook
    end

    header = [record, length].pack('vv')
    data   = [cch, rgch].pack('CC')

    prepend(header, data, sheetname)
  end