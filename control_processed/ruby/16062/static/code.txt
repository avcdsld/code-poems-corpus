def init_config(loader)
      case loader
      when String, Hash, nil
        @config_loader = ConfigLoaders::FileOrHashLoader.new(loader)
      else
        @config_loader = loader
      end
      load_config
    end