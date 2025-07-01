def store_pos(mdTopLt, mdBotRt, x1, y1, x2, y2)  # :nodoc:
    record  = 0x104F     # Record identifier.
    length  = 0x0014     # Number of bytes to follow.
    # mdTopLt            # Top left.
    # mdBotRt            # Bottom right.
    # x1                 # X coordinate.
    # y1                 # Y coordinate.
    # x2                 # Width.
    # y2                 # Height.

    header = [record, length].pack('vv')
    data  = [mdTopLt].pack('v')
    data += [mdBotRt].pack('v')
    data += [x1].pack('V')
    data += [y1].pack('V')
    data += [x2].pack('V')
    data += [y2].pack('V')

    append(header, data)
  end