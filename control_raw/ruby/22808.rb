def play(file_or_url, options = {})
      @players = @devices.map { |device| device.play(file_or_url, options) }
      Players.new(@players)
    end