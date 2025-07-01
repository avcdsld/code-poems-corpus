def prepend_env(cmd)
      return cmd unless @rye_current_environment_variables.is_a?(Hash)
      env = ''
      @rye_current_environment_variables.each_pair do |n,v|
        env << "export #{n}=#{Escape.shell_single_word(v)}; "
      end
      [env, cmd].join(' ')
    end