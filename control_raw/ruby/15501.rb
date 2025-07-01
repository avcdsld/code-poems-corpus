def check_root!
      unless root.nil? || (root.is_a?(String) && !root.strip.empty?) || root.is_a?(Symbol)
        Surrealist::ExceptionRaiser.raise_invalid_root!(root)
      end
    end