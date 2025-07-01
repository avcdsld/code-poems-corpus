def receive_data(data)
      #append data to buffer
      @data << data

      while (@data.length >=4)
        cmd_length = @data[0..3].unpack('N').first
        if(@data.length < cmd_length)
          #not complete packet ... break
          break
        end

        pkt = @data.slice!(0,cmd_length)

        begin
          # parse incoming PDU
          pdu = read_pdu(pkt)

          # let subclass process it
          process_pdu(pdu) if pdu
        rescue Exception => e
          logger.error "Error receiving data: #{e}\n#{e.backtrace.join("\n")}"
          run_callback(:data_error, e)
        end

      end
    end