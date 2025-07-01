def iterated_dominance_frontier(set, dom_tree)
      worklist = Set.new(set)
      result = Set.new(set)
      frontier = dominance_frontier(dom_tree)

      until worklist.empty?
        block = worklist.pop
        frontier[dom_tree[block]].each do |candidate|
          candidate_in_full_graph = self[candidate]
          unless result.include?(candidate_in_full_graph)
            result << candidate_in_full_graph
            worklist << candidate_in_full_graph
          end
        end
      end
      result
    end