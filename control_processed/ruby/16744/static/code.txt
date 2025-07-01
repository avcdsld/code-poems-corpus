def parent_breadcrumb(options = {}, &block)
      if block_given?
        gretel_renderer.yield_parent_breadcrumb(options, &block)
      else
        gretel_renderer.parent_breadcrumb(options)
      end
    end