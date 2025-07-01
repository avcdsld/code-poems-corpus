def validate_host_port(action)
      raise JSS::UnsupportedError, "Cannot #{action} without first setting a host_name and port" if host_name.to_s.empty? || port.to_s.empty?
    end