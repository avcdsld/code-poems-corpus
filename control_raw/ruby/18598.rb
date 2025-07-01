def new_link(model_class, html_options: {}, &block)
      return if unauthorized? :new, model_class
      html_options, block = LinkOptionsNormalizer.normalize(
        html_options, block,
        class: 'resource__create',
        block: -> { t 'links.new', model: to_model_label(model_class) }
      )

      link_to new_path(model_class), html_options, &block
    end