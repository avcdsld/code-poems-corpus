def send_apdu(apdu)
    	cmd = apdu
    	cmd.force_encoding('ASCII-8BIT')
			command_buffer = FFI::MemoryPointer.new(:uint8, cmd.length)
			command_buffer.write_string_length(cmd, cmd.length)

			response_buffer = FFI::MemoryPointer.new(:uint8, 254)

			res_len = LibNFC.nfc_initiator_transceive_bytes(@reader.ptr,
				command_buffer, cmd.length, response_buffer, 254, 0)

			raise IsoDep::Error, "APDU sending failed: #{res_len}" if res_len < 0

			APDU::Response.new(response_buffer.get_bytes(0, res_len).to_s)
    end