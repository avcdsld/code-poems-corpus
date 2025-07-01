def title
      @title ||= begin
        if options[:title]
          options[:title]
        else
          title_builder = ''
          title_builder << "#{options[:value]} " if options[:value].is_a?(Symbol)
          title_builder << (options[:category].is_a?(Symbol) ? "per #{options[:category]}" : 'per request')
          title_builder
        end
      end
    end