def decode(length, type)
      raise ArgumentError, "Invalid argument length. Expected Integer, got #{length.class}" unless length.is_a?(Integer)
      raise ArgumentError, "Invalid argument type. Expected string, got #{type.class}" unless type.is_a?(String)
      value = nil
      if (@index + length) <= @string.length
        # There are sufficient bytes remaining to extract the value:
        if type == 'AT'
          # We need to guard ourselves against the case where a string contains an invalid 'AT' value:
          if length == 4
            value = decode_tag
          else
            # Invalid. Just return nil.
            skip(length)
          end
        else
          # Decode the binary string and return value:
          value = @string.slice(@index, length).unpack(vr_to_str(type))
          # If the result is an array of one element, return the element instead of the array.
          # If result is contained in a multi-element array, the original array is returned.
          if value.length == 1
            value = value[0]
            # If value is a string, strip away possible trailing whitespace:
            value = value.rstrip if value.is_a?(String)
          end
          # Update our position in the string:
          skip(length)
        end
      end
      value
    end