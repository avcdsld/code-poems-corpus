def source_code
      next_node_line =
        if next_node
          next_node.line - 1
        else
          @document.source_lines.count + 1
        end

      @document.source_lines[@line - 1...next_node_line]
               .join("\n")
               .gsub(/^\s*\z/m, '') # Remove blank lines at the end
    end