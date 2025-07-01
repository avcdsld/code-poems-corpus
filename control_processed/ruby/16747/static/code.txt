def links_for_render(options = {})
      out = links.dup

      # Handle autoroot
      if options[:autoroot] && out.map(&:key).exclude?(:root) && Gretel::Crumbs.crumb_defined?(:root)
        out.unshift *Gretel::Crumb.new(context, :root).links
      end

      # Set current link to actual path
      if options[:link_current_to_request_path] && out.any? && request
        out.last.url = request.fullpath
      end

      # Handle show root alone
      if out.size == 1 && !options[:display_single_fragment]
        out.shift
      end

      # Set last link to current
      out.last.try(:current!)

      out
    end