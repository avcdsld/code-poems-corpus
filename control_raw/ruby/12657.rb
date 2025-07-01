def nest_seqs(root)
      current_rule = nil
      root.children.map! do |child|
        unless child.is_a?(Tree::RuleNode)
          nest_seqs(child) if child.is_a?(Tree::DirectiveNode)
          next child
        end

        seq = first_seq(child)
        seq.members.reject! {|sseq| sseq == "\n"}
        first, rest = seq.members.first, seq.members[1..-1]

        if current_rule.nil? || first_sseq(current_rule) != first
          current_rule = Tree::RuleNode.new([])
          current_rule.parsed_rules = make_seq(first)
        end

        if rest.empty?
          current_rule.children += child.children
        else
          child.parsed_rules = make_seq(*rest)
          current_rule << child
        end

        current_rule
      end
      root.children.compact!
      root.children.uniq!

      root.children.each {|v| nest_seqs(v)}
    end