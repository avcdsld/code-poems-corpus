def interpret_command_and_data(message, file=nil)
      info = Hash.new
      msg = Stream.new(message, @net_endian)
      # Length (of remaining PDV data) (4 bytes)
      info[:presentation_data_value_length] = msg.decode(4, "UL")
      # Calculate the last index position of this message element:
      last_index = info[:presentation_data_value_length] + msg.index
      # Presentation context ID (1 byte)
      info[:presentation_context_id] = msg.decode(1, "BY")
      @presentation_context_id = info[:presentation_context_id]
      # Flags (1 byte)
      info[:presentation_context_flag] = msg.decode(1, "HEX") # "03" for command (last fragment), "02" for data
      # Apply the proper transfer syntax for this presentation context:
      set_transfer_syntax(@presentation_contexts[info[:presentation_context_id]])
      # "Data endian" encoding from now on:
      msg.endian = @data_endian
      # We will put the results in a hash:
      results = Hash.new
      if info[:presentation_context_flag] == COMMAND_LAST_FRAGMENT
        # COMMAND, LAST FRAGMENT:
        while msg.index < last_index do
          # Tag (4 bytes)
          tag = msg.decode_tag
          # Length (2 bytes)
          length = msg.decode(2, "US")
          if length > msg.rest_length
            logger.error("Specified length of command element value exceeds remaining length of the received message! Something is wrong.")
          end
          # Reserved (2 bytes)
          msg.skip(2)
          # VR (from library - not the stream):
          vr = LIBRARY.element(tag).vr
          # Value (variable length)
          value = msg.decode(length, vr)
          # Put tag and value in a hash:
          results[tag] = value
        end
        # The results hash is put in an array along with (possibly) other results:
        info[:results] = results
        # Store the results in an instance variable (to be used later when sending a receipt for received data):
        @command_request = results
        # Check if the command fragment indicates that this was the last of the response fragments for this query:
        status = results["0000,0900"]
        if status
          # Note: This method will also stop the packet receiver if indicated by the status mesasge.
          process_status(status)
        end
        # Special case: Handle a possible C-ECHO-RQ:
        if info[:results]["0000,0100"] == C_ECHO_RQ
          logger.info("Received an Echo request. Returning an Echo response.")
          handle_response
        end
      elsif info[:presentation_context_flag] == DATA_MORE_FRAGMENTS or info[:presentation_context_flag] == DATA_LAST_FRAGMENT
        # DATA FRAGMENT:
        # If this is a file transmission, we will delay the decoding for later:
        if file
          # Just store the binary string:
          info[:bin] = msg.rest_string
          # If this was the last data fragment of a C-STORE, we need to send a receipt:
          # (However, for, say a C-FIND-RSP, which indicates the end of the query results, this method shall not be called) (Command Field (0000,0100) holds information on this)
          handle_response if info[:presentation_context_flag] == DATA_LAST_FRAGMENT
        else
          # Decode data elements:
          while msg.index < last_index do
            # Tag (4 bytes)
            tag = msg.decode_tag
            if @explicit
              # Type (VR) (2 bytes):
              type = msg.decode(2, "STR")
              # Length (2 bytes)
              length = msg.decode(2, "US")
            else
              # Implicit:
              type = nil # (needs to be defined as nil here or it will take the value from the previous step in the loop)
              # Length (4 bytes)
              length = msg.decode(4, "UL")
            end
            if length > msg.rest_length
              logger.error("The specified length of the data element value exceeds the remaining length of the received message!")
            end
            # Fetch type (if not defined already) for this data element:
            type = LIBRARY.element(tag).vr unless type
            # Value (variable length)
            value = msg.decode(length, type)
            # Put tag and value in a hash:
            results[tag] = value
          end
          # The results hash is put in an array along with (possibly) other results:
          info[:results] = results
        end
      else
        # Unknown.
        logger.error("Unknown presentation context flag received in the query/command response. (#{info[:presentation_context_flag]})")
        stop_receiving
      end
      # If only parts of the string was read, return the rest:
      info[:rest_string] = msg.rest_string if last_index < msg.length
      info[:valid] = true
      return info
    end