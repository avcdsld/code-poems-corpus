def serve
      # Note, looks like stopping jets server with Ctrl-C sends the TERM signal
      # down to the sub bin/rackup command cleans up the child process fine.
      Bundler.with_clean_env do
        args = ''
        # only forward the host option, port is always 9292 for simplicity
        if @options[:host]
          args << " --host #{@options[:host]}"
        else
          args << " --host 127.0.0.1" # using the default localhost is not starting up https://stackoverflow.com/questions/4356646/address-family-not-supported-by-protocol-family
        end


        command = "cd #{rack_project} && bin/rackup#{args}" # leads to the same wrapper rack scripts
        puts "=> #{command}".color(:green)
        system(command)
      end
    end