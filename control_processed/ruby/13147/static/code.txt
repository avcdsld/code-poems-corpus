def render_element(*args)
      if args.length == 4
        element, _part, options, counter = *args
        Alchemy::Deprecation.warn "passing a `part` parameter as second argument to `render_element` has been removed without replacement. " \
          "You can safely remove it."
      else
        element, options, counter = *args
      end

      options ||= {}
      counter ||= 1

      if element.nil?
        warning('Element is nil')
        render "alchemy/elements/view_not_found", {name: 'nil'}
        return
      end

      element.store_page(@page)

      render element, {
        element: element,
        counter: counter,
        options: options
      }.merge(options.delete(:locals) || {})
    rescue ActionView::MissingTemplate => e
      warning(%(
        Element view partial not found for #{element.name}.\n
        #{e}
      ))
      render "alchemy/elements/view_not_found", name: element.name
    end