def render
      return render_no_object_warning if list_item.object? && !object_available?

      content_tag opts[:wrapper_element], class: html_classes do
        if list_item.has_children?
          concat render_item
          concat content_tag opts[:child_wrapper_element], render_children, { class: opts[:child_wrapper_class] }, false
        else
          render_item
        end
      end
    end