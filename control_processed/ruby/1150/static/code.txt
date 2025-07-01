def shared_logical_id
      regexp = Regexp.new(".*#{Jets.config.project_namespace}-shared-") # remove the shared
      shared_name = @path.sub(regexp, '').sub('.yml', '')
      shared_name.underscore.camelize
    end