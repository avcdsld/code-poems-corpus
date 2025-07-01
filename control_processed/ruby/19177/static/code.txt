def env
      env_hash = {}
      env_hash["NODE_PATH"] = asset_paths unless uses_exorcist
      env_hash["NODE_ENV"] = config.node_env || Rails.env
      env_hash
    end