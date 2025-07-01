def run
      if PryNav.current_remote_server
        raise 'Already running a pry-remote session!'
      else
        PryNav.current_remote_server = self
      end

      setup
      Pry.start @object, {
        :input  => client.input_proxy,
        :output => client.output,
        :pry_remote => true
      }
    end