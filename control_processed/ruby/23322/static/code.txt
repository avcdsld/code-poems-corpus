def render_with_overrides(*args, &block)
      options = args.extract_options!
      name = args.first
      if name.is_a?(Symbol) || name.is_a?(String)
        # TODO: block needs to be handled differently so as to provide overrides
        block_with_hooks_renderer.render(*args, options, &block)
      elsif options[:partial]
        partial_renderer.render(options.delete(:partial), options, &block)
      else
        # TODO: handle other possible rendering methods such as a custom renderer
      end
    end