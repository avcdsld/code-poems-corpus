def save(filename)
      speech = bytes_wav
      res = IO.popen(lame_command(filename, command_options), 'r+') do |process|
        process.write(speech)
        process.close_write
        process.read
      end
      res.to_s
    end