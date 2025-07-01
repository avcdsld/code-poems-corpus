def view what, config={}, &block # :yields: textview for further configuration
        require 'canis/core/util/viewer'
        Canis::Viewer.view what, config, &block
      end