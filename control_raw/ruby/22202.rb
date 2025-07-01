def start_suite(suite)
      @suite  = suite
      @time   = Time.now

      io.puts Colorize.bold("Loaded Suite #{suite.name}")
      io.puts
      if suite.seed
        io.puts "Started at #{Time.now} w/ seed #{suite.seed}."
      else
        io.puts "Started at #{Time.now}."
      end
      io.puts
    end