def set_aws_profile!
      return if ENV['TEST']
      return unless File.exist?("#{Ufo.root}/.ufo/settings.yml") # for rake docs
      return unless settings # Only load if within Ufo project and there's a settings.yml
      data = settings[Ufo.env] || {}
      if data["aws_profile"]
        puts "Using AWS_PROFILE=#{data["aws_profile"]} from UFO_ENV=#{Ufo.env} in config/settings.yml"
        ENV['AWS_PROFILE'] = data["aws_profile"]
      end
    end