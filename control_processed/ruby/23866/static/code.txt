def clone_tree_without_branch node
      new_tree = self.class.new
      original = [root] + root.descendents
      # p "Original",original
      skip = [node] + node.descendents
      # p "Skip",skip
      # p "Retain",root.descendents - skip
      nodes.each do |x|
        if not skip.include?(x)
          new_tree.add_node(x) 
        else
        end
      end
      each_edge do |node1, node2, edge|
        if new_tree.include?(node1) and new_tree.include?(node2) 
          new_tree.add_edge(node1, node2, edge)
        end
      end
      new_tree
    end