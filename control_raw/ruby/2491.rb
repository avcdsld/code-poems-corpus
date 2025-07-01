def add_to_guardfile
      klass = plugin_class # call here to avoid failing later

      require_relative "guardfile/evaluator"
      # TODO: move this to Generator?
      options = Guard.state.session.evaluator_options
      evaluator = Guardfile::Evaluator.new(options)
      begin
        evaluator.evaluate
      rescue Guard::Guardfile::Evaluator::NoPluginsError
      end

      if evaluator.guardfile_include?(name)
        UI.info "Guardfile already includes #{ name } guard"
      else
        content = File.read("Guardfile")
        File.open("Guardfile", "wb") do |f|
          f.puts(content)
          f.puts("")
          f.puts(klass.template(plugin_location))
        end

        UI.info INFO_ADDED_GUARD_TO_GUARDFILE % name
      end
    end