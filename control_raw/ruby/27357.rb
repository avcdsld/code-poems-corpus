def validate_dependencies
      Spiceweasel::Log.debug("cookbook validate_dependencies: '#{@dependencies}'")
      @dependencies.each do |dep|
        unless member?(dep)
          STDERR.puts "ERROR: Cookbook dependency '#{dep}' is missing from the list of cookbooks in the manifest."
          exit(-1)
        end
      end
    end