def add_comment(path, position, message, severity)
      stripped_path = path.strip

      raise GergichError, "invalid position `#{position}`" unless valid_position?(position)
      position = position.to_json if position.is_a?(Hash)
      raise GergichError, "invalid severity `#{severity}`" unless SEVERITY_MAP.key?(severity)
      raise GergichError, "no message specified" unless message.is_a?(String) && !message.empty?

      db.execute "INSERT INTO comments (path, position, message, severity) VALUES (?, ?, ?, ?)",
                 [stripped_path, position, message, severity]
    end