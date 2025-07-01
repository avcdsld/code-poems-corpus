def run
      Jekyll.logger.debug "Rendering:", document.relative_path

      assign_pages!
      assign_current_document!
      assign_highlighter_options!
      assign_layout_data!

      Jekyll.logger.debug "Pre-Render Hooks:", document.relative_path
      document.trigger_hooks(:pre_render, payload)

      render_document
    end