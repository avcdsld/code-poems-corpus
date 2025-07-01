def load_yaml_file(file_type, file_name)
      YAML.load_file file_name
    rescue StandardError => error
      @logger.error "Cannot load #{file_type}: #{file_name}"
      raise error
    end