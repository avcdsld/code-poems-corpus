def link_to_each_facet_field(options)
      config = options.fetch(:config)
      separator = config.fetch(:separator, ' > ')
      output_separator = config.fetch(:output_separator, separator)
      facet_search = config.fetch(:helper_facet)
      facet_fields = Array.wrap(options.fetch(:value)).first.split(separator).map(&:strip)

      facet_links = facet_fields.map do |type|
        link_to(type, main_app.search_catalog_path(f: { facet_search => [type] }))
      end
      safe_join(facet_links, output_separator)
    end