def handle_incoming_data(path)
      # Wait for incoming data:
      segments = receive_multiple_transmissions(file=true)
      # Reset command results arrays:
      @command_results = Array.new
      @data_results = Array.new
      file_transfer_syntaxes = Array.new
      files = Array.new
      single_file_data = Array.new
      # Proceed to extract data from the captured segments:
      segments.each do |info|
        if info[:valid]
          # Determine if it is command or data:
          if info[:presentation_context_flag] == DATA_MORE_FRAGMENTS
            @data_results << info[:results]
            single_file_data  << info[:bin]
          elsif info[:presentation_context_flag] == DATA_LAST_FRAGMENT
            @data_results << info[:results]
            single_file_data  << info[:bin]
            # Join the recorded data binary strings together to make a DICOM file binary string and put it in our files Array:
            files << single_file_data.join
            single_file_data = Array.new
          elsif info[:presentation_context_flag] == COMMAND_LAST_FRAGMENT
            @command_results << info[:results]
            @presentation_context_id = info[:presentation_context_id] # Does this actually do anything useful?
            file_transfer_syntaxes << @presentation_contexts[info[:presentation_context_id]]
          end
        end
      end
      # Process the received files using the customizable FileHandler class:
      success, messages = @file_handler.receive_files(path, files, file_transfer_syntaxes)
      return success, messages
    end