def generate(&block)
      create_temp_dir
      if block
        instance_eval &block
      else
        instance_eval open(DynamicSitemaps.config_path).read, DynamicSitemaps.config_path
      end
      generate_index
      move_to_destination
      ping_search_engines
    ensure
      remove_temp_dir
    end