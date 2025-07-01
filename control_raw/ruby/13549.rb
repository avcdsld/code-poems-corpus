def refresh_crumbs(force_refresh = false)
      # Quick check to see if someone has changed XSS settings and not
      # restarted us
      if force_refresh || @crumbs_enabled.nil?
        old_crumbs_setting = @crumbs_enabled
        new_crumbs_setting = use_crumbs?

        if old_crumbs_setting != new_crumbs_setting
          @crumbs_enabled = new_crumbs_setting
        end

        # Get or clear crumbs setting appropriately
        # Works as refresh if crumbs still enabled
        if @crumbs_enabled
          if old_crumbs_setting
            @logger.info "Crumb expired.  Refetching from the server."
          else
            @logger.info "Crumbs turned on.  Fetching from the server."
          end

          @crumb = get_crumb if force_refresh || !old_crumbs_setting
        else
          if old_crumbs_setting
            @logger.info "Crumbs turned off.  Clearing crumb."
            @crumb.clear
          end
        end
      end
    end