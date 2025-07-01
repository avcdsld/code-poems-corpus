def append_user_information(ui)
      # USER INFORMATION:
      # User information item type (1 byte)
      @outgoing.encode_last(ITEM_USER_INFORMATION, "HEX")
      # Reserved (1 byte)
      @outgoing.encode_last("00", "HEX")
      # Encode the user information item values so we can determine the remaining length of this section:
      values = Array.new
      ui.each_index do |i|
        values << @outgoing.encode(ui[i][2], ui[i][1])
      end
      # User information item length (2 bytes)
      items_length = 4*ui.length + values.join.length
      @outgoing.encode_last(items_length, "US")
      # SUB-ITEMS:
      ui.each_index do |i|
        # UI item type (1 byte)
        @outgoing.encode_last(ui[i][0], "HEX")
        # Reserved (1 byte)
        @outgoing.encode_last("00", "HEX")
        # UI item length (2 bytes)
        @outgoing.encode_last(values[i].length, "US")
        # UI value (4 bytes)
        @outgoing.add_last(values[i])
      end
    end