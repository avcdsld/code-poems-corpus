def acquire_password(args)
      if args[:pw] == :prompt
        JSS.prompt_for_password "Enter the password for JSS user #{args[:user]}@#{args[:server]}:"
      elsif args[:pw].is_a?(Symbol) && args[:pw].to_s.start_with?('stdin')
        args[:pw].to_s =~ /^stdin(\d+)$/
        line = Regexp.last_match(1)
        line ||= 1
        JSS.stdin line
      else
        args[:pw]
      end
    end