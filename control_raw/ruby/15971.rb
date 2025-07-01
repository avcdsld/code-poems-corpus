def find_title(title, options = {})
      return title if title.nil? || title.empty?

      options[:scope] ||= translation_scope
      options[:default] = Array(options[:default])
      options[:default] << title if options[:default].empty?
      I18n.t(title.to_s, options)
    end