def read_yaml(base, name, opts = {})
      filename = File.join(base, name)

      begin
        self.content = File.read(@path || site.in_source_dir(base, name),
                                 Utils.merged_file_read_opts(site, opts))
        if content =~ Document::YAML_FRONT_MATTER_REGEXP
          self.content = $POSTMATCH
          self.data = SafeYAML.load(Regexp.last_match(1))
        end
      rescue SyntaxError => e
        Bunto.logger.warn "YAML Exception reading #{filename}: #{e.message}"
      rescue => e
        Bunto.logger.warn "Error reading file #{filename}: #{e.message}"
      end

      self.data ||= {}

      validate_data! filename
      validate_permalink! filename

      self.data
    end