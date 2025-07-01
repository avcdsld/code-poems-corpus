def eval_context(context, node)
      node.context(&context[:block]) if context[:nodes].matches?(node.name)
    end