def execute
      return if should_skip?

      print "[#{@runner.step_num}] Verifying display server ... "

      if @runner.is_linux? && !@runner.xvfb_installed?
        return puts "Warning (XVFB is not installed.  Feature specs will fail.)".colorize(:yellow)
      end

      if @runner.is_mac? && @runner.xvfb_installed?
        return puts "Warning (XVFB has been installed.  It's not needed on a Mac and may cause specs to fail.)".colorize(:yellow)
      end

      puts "Success!!".colorize(:green)
    end