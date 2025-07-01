def remove_vertex(u)
      u.clear_edges
      looked_up = self[u]
      # looked_up.successors.each do |succ|
      #   self[succ].remove_predecessor looked_up
      #   self[looked_up].delete_all_flags succ
      # end
      # looked_up.predecessors.each do |pred|
      #   self[pred].remove_successor looked_up
      #   self[pred].delete_all_flags looked_up
      # end
      @vertex_lookup.delete looked_up.name
      vertices.delete looked_up
    end