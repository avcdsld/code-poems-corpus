def transcode_movie
      FFMPEG.logger.info("Running transcoding...\n#{command}\n")
      @output = ""

      Open3.popen3(*command) do |_stdin, _stdout, stderr, wait_thr|
        begin
          yield(0.0) if block_given?
          next_line = Proc.new do |line|
            fix_encoding(line)
            @output << line
            if line.include?("time=")
              if line =~ /time=(\d+):(\d+):(\d+.\d+)/ # ffmpeg 0.8 and above style
                time = ($1.to_i * 3600) + ($2.to_i * 60) + $3.to_f
              else # better make sure it wont blow up in case of unexpected output
                time = 0.0
              end

              if @movie
                progress = time / @movie.duration
                yield(progress) if block_given?
              end
            end
          end

          if timeout
            stderr.each_with_timeout(wait_thr.pid, timeout, 'size=', &next_line)
          else
            stderr.each('size=', &next_line)
          end

        @errors << "ffmpeg returned non-zero exit code" unless wait_thr.value.success?

        rescue Timeout::Error => e
          FFMPEG.logger.error "Process hung...\n@command\n#{command}\nOutput\n#{@output}\n"
          raise Error, "Process hung. Full output: #{@output}"
        end
      end
    end