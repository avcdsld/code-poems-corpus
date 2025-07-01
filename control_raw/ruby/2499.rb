def logger(options)
      if options[:level]
        options[:level] = options[:level].to_sym

        unless [:debug, :info, :warn, :error].include? options[:level]
          UI.warning(format(WARN_INVALID_LOG_LEVEL, options[:level]))
          options.delete :level
        end
      end

      if options[:only] && options[:except]
        UI.warning WARN_INVALID_LOG_OPTIONS

        options.delete :only
        options.delete :except
      end

      # Convert the :only and :except options to a regular expression
      [:only, :except].each do |name|
        next unless options[name]

        list = [].push(options[name]).flatten.map do |plugin|
          Regexp.escape(plugin.to_s)
        end

        options[name] = Regexp.new(list.join("|"), Regexp::IGNORECASE)
      end

      UI.options = UI.options.merge(options)
    end