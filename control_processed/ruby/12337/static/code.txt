def destroy(force = false)
      if (!force && file =~ /\.yardoc$/) || force
        if File.file?(@file)
          # Handle silent upgrade of old .yardoc format
          File.unlink(@file)
        elsif File.directory?(@file)
          FileUtils.rm_rf(@file)
        end
        true
      else
        false
      end
    end