def dump_selectors(root)
      root.children.each do |child|
        next dump_selectors(child) if child.is_a?(Tree::DirectiveNode)
        next unless child.is_a?(Tree::RuleNode)
        child.rule = [child.parsed_rules.to_s]
        dump_selectors(child)
      end
    end