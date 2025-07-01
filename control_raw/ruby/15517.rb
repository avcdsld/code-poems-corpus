def write(key_hash, value)
      return value if value.nil? || value.empty?
      File.open(key_path(key_hash), 'wb') do |f|
        Marshal.dump(value, f)
      end

      value
    end