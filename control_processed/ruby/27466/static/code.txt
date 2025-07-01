def clean!
      stop
      remove_instance_dir!
      FileUtils.remove_entry(config.download_path) if File.exists?(config.download_path)
      FileUtils.remove_entry(config.tmp_save_dir, true) if File.exists? config.tmp_save_dir
      md5.clean!
      FileUtils.remove_entry(config.version_file) if File.exists? config.version_file
    end