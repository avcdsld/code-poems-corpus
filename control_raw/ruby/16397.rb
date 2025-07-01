def find_by_tag_id(tag_id)
      @nodes.each do |node|
        if node.is_a?(ComponentNode)
          # Walk down nodes
          val = node.find_by_tag_id(tag_id)
          return val if val
        elsif node.is_a?(TagNode)
          # Found a matching tag
          return node if node.tag_id == tag_id
        end
      end

      nil
    end