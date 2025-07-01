def on_block(node)
      builder    = DefinitionBuilder::RubyBlock.new(node, self)
      definition = builder.build

      associate_node(node, definition)

      push_scope(definition)
    end