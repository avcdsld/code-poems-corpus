def markup
      # Use display_path if defined, otherwise use output_path in url
      display_path = @options['display_path'] || @options['output_path']

      @html = @assets.map do |asset|
        klass = JAPR::Template.klass(asset.filename)
        html = klass.new(display_path, asset.filename).html unless klass.nil?

        html
      end.join
    end