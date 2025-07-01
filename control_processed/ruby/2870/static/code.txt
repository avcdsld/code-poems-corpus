def following_node_line(node)
      [
        [node.children.first, next_node(node)].compact.map(&:line),
        @document.source_lines.count + 1,
      ].flatten.min
    end