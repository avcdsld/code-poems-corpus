def diagnose filename
      # @todo Only open files get diagnosed. Determine whether anything or
      #   everything in the workspace should get diagnosed, or if there should
      #   be an option to do so.
      #
      return [] unless open?(filename)
      catalog
      result = []
      source = read(filename)
      workspace.config.reporters.each do |name|
        reporter = Diagnostics.reporter(name)
        raise DiagnosticsError, "Diagnostics reporter #{name} does not exist" if reporter.nil?
        result.concat reporter.new.diagnose(source, api_map)
      end
      result
    end