def video_resolution(video_path)
      command = "ffmpeg -i \"#{video_path}\" 2>&1"
      # puts "COMMAND: #{command}"
      output = `#{command}`
      # Note: ffmpeg exits with 1 if no output specified
      # raise "Failed to find video information from #{video_path} (using #{command})" unless $CHILD_STATUS.to_i == 0
      output = output.force_encoding("BINARY")
      video_infos = output.split("\n").select { |l| l =~ /Stream.*Video/ }
      raise "Unable to find Stream Video information from ffmpeg output of #{command}" if video_infos.count == 0
      video_info = video_infos[0]
      res = video_info.match(/.* ([0-9]+)x([0-9]+).*/)
      raise "Unable to parse resolution information from #{video_info}" if res.size < 3
      [res[1].to_i, res[2].to_i]
    end