def append(type, val)
      raise TypeException, "Cannot send nil" if val.nil?

      type = type.chr if type.is_a?(Integer)
      type = Type::Parser.new(type).parse[0] if type.is_a?(String)
      case type.sigtype
      when Type::BYTE
        @packet += val.chr
      when Type::UINT32, Type::UNIX_FD
        align(4)
        @packet += [val].pack("L")
      when Type::UINT64
        align(8)
        @packet += [val].pack("Q")
      when Type::INT64
        align(8)
        @packet += [val].pack("q")
      when Type::INT32
        align(4)
        @packet += [val].pack("l")
      when Type::UINT16
        align(2)
        @packet += [val].pack("S")
      when Type::INT16
        align(2)
        @packet += [val].pack("s")
      when Type::DOUBLE
        align(8)
        @packet += [val].pack("d")
      when Type::BOOLEAN
        align(4)
        @packet += if val
                     [1].pack("L")
                   else
                     [0].pack("L")
                   end
      when Type::OBJECT_PATH
        append_string(val)
      when Type::STRING
        append_string(val)
      when Type::SIGNATURE
        append_signature(val)
      when Type::VARIANT
        vartype = nil
        if val.is_a?(Array) && val.size == 2
          if val[0].is_a?(DBus::Type::Type)
            vartype, vardata = val
          elsif val[0].is_a?(String)
            begin
              parsed = Type::Parser.new(val[0]).parse
              vartype = parsed[0] if parsed.size == 1
              vardata = val[1]
            rescue Type::SignatureException
              # no assignment
            end
          end
        end
        if vartype.nil?
          vartype, vardata = PacketMarshaller.make_variant(val)
          vartype = Type::Parser.new(vartype).parse[0]
        end

        append_signature(vartype.to_s)
        align(vartype.alignment)
        sub = PacketMarshaller.new(@offset + @packet.bytesize)
        sub.append(vartype, vardata)
        @packet += sub.packet
      when Type::ARRAY
        if val.is_a?(Hash)
          raise TypeException, "Expected an Array but got a Hash" if type.child.sigtype != Type::DICT_ENTRY
          # Damn ruby rocks here
          val = val.to_a
        end
        # If string is recieved and ay is expected, explode the string
        if val.is_a?(String) && type.child.sigtype == Type::BYTE
          val = val.bytes
        end
        if !val.is_a?(Enumerable)
          raise TypeException, "Expected an Enumerable of #{type.child.inspect} but got a #{val.class}"
        end
        array(type.child) do
          val.each do |elem|
            append(type.child, elem)
          end
        end
      when Type::STRUCT, Type::DICT_ENTRY
        # TODO: use duck typing, val.respond_to?
        raise TypeException, "Struct/DE expects an Array" if !val.is_a?(Array)
        if type.sigtype == Type::DICT_ENTRY && val.size != 2
          raise TypeException, "Dict entry expects a pair"
        end
        if type.members.size != val.size
          raise TypeException, "Struct/DE has #{val.size} elements but type info for #{type.members.size}"
        end
        struct do
          type.members.zip(val).each do |t, v|
            append(t, v)
          end
        end
      else
        raise NotImplementedError,
              "sigtype: #{type.sigtype} (#{type.sigtype.chr})"
      end
    end