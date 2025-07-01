def synx_installed?
      match = `#{synx} --version`.match(/Synx (\d+)\.(\d+)\.(\d+)/i)
      if match
        major, minor, patch = match.captures.map { |c| Integer(c) }
        major > 0 || minor > 2 || (minor == 2 && patch > 1)
      else
        false
      end
    end