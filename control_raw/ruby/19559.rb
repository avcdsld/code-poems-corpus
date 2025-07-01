def write_url_external_net(row1, col1, row2, col2, url, str, format)       #:nodoc:
    record      = 0x01B8                       # Record identifier
    length      = 0x00000                      # Bytes to follow

    xf          = format || url_format  # The cell format

    # Strip URL type and change Unix dir separator to Dos style (if needed)
    #
    url = url.sub(/^external:/, '').gsub!(%r|/|, '\\')

    # Write the visible label but protect against url recursion in write().
    str = url.sub(/\#/, ' - ') unless str
    error        = write_string(row1, col1, str, xf)
    return error if error == -2

    dir_long, link_type, sheet_len, sheet = analyze_link(url)

    # Pack the link type
    link_type      = [link_type].pack("V")

    # Make the string null terminated
    dir_long      += "\0"

    # Pack the lengths of the dir string
    dir_long_len  = [dir_long.bytesize].pack("V")

    # Store the long dir name as a wchar string (non-null terminated)
    dir_long = dir_long.split('').join("\0") + "\0"

    # Pack the undocumented part of the hyperlink stream
    unknown1    = ['D0C9EA79F9BACE118C8200AA004BA90B02000000'].pack("H*")

    # Pack the main data stream
    data         = [row1, row2, col1, col2].pack("vvvv") +
    unknown1     +
    link_type    +
    dir_long_len +
    dir_long     +
    sheet_len    +
    sheet

    # Pack the header data
    length      = data.bytesize
    header      = [record, length].pack("vv")

    # Write the packed data
    append(header, data)

    error
  end