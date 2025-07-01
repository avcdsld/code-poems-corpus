def value=(path)
      path = path.gsub(File::SEPARATOR, File::ALT_SEPARATOR) if File::ALT_SEPARATOR
      element_call { @element.send_keys path }
    end