def status_line config={}, &block
      require 'canis/core/widgets/statusline'
      sl = Canis::StatusLine.new @form, config, &block
    end