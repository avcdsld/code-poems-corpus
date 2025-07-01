def check_for_libraries
      output = []

      required_libraries.each do |library|
        begin
          require library
        rescue LoadError
          install_command = @config['install_command']
          install_command = " -- install via #{install_command}" if install_command

          output << "Unable to load '#{library}'#{install_command}"
        end
      end

      return if output.empty?

      output.join("\n")
    end