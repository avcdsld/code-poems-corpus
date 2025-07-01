def parse_config(config)
      sections = {"defaults" => []}
      current  = "defaults"
      config.gsub(/#[^\n]*/, "")
        .split(/\n/)
        .map(&:strip)
        .reject(&:empty?)
        .each do |line|
        if IS_SECTION =~ line
          current = line.match(IS_SECTION)[1].strip
          sections[current] ||= []
        else
          sections[current] << line
        end
      end
      sections
    end