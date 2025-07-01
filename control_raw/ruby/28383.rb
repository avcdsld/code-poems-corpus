def render
      # Initialize the resulting tag
      tag_parts = []

      # Slice objects into separate lists
      lists = slice_objects

      # Render each list into `tag` variable
      lists.each do |list|
        items = list.collect { |item| render_link_for(item) }
        tag_parts << render_content_tag_for(items)
      end

      tag_parts.join.html_safe
    end