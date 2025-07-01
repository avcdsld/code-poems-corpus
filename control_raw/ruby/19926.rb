def transmit
      transmitter = Transmitter.new(ACTION, config)
      puts "Notifying AppSignal of deploy with: "\
        "revision: #{marker_data[:revision]}, user: #{marker_data[:user]}"

      response = transmitter.transmit(marker_data)
      unless response.code == "200"
        raise "#{response.code} at #{transmitter.uri}"
      end
      puts "AppSignal has been notified of this deploy!"
    rescue => e
      puts "Something went wrong while trying to notify AppSignal: #{e}"
    end