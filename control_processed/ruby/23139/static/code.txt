def extract_front_matter(source)
      fm_regex = /\A(---\s*\n.*?\n?)^(---\s*$\n?)/m

      return [{}, source] unless match = source.match(fm_regex)

      source = source.sub(fm_regex, "")

      begin
        data = (YAML.safe_load(match[1]) || {}).inject({}) do |memo, (k, v)|
          memo[k.to_sym] = v
          memo
        end
      rescue *YAML_ERRORS => e
        puts "YAML Exception: #{e.message}"
        return false
      end

      [data, source]
    rescue
      [{}, source]
    end