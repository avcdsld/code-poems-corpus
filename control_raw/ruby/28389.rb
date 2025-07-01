def print_rule(rule)
      unless rule.file_exists
        log_red "  #{rule.file}:", false
        log_red " '#{rule.before_pattern}' (file not found)"

        return
      end

      log "  #{rule.file}:", false

      unless rule.pattern_exists
        log_red " '#{rule.before_pattern}' (pattern not found)"

        return
      end

      log_green " '#{rule.before_pattern}'"
    end