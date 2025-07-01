def colorize(params)
      return self if self.class.disable_colorization
      require_windows_libs
      scan_for_colors.inject(self.class.new) do |str, match|
        colors_from_params(match, params)
        defaults_colors(match)
        str << "\033[#{match[0]};#{match[1]};#{match[2]}m#{match[3]}\033[0m"
      end
    end