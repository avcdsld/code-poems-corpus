def visit_CommandNode(node)
      debug_visit(node)
      @aliases_expanded ||= []
      @command_node_args_stack ||= []
      with_standard_streams do |stdin, stdout, stderr|
        args = process_ArgumentNodes(node.args)
        if !node.literal? && !@aliases_expanded.include?(node.command) && Aliases.instance.has_key?(node.command)
          _alias=Aliases.instance.fetch_alias(node.command)
          @suppress_events = true
          @command_node_args_stack << args
          ast = Parser.parse(_alias)
          @aliases_expanded.push(node.command)
          ast.accept(self)
          @aliases_expanded.pop
          @suppress_events = false
        else
          cmd2execute = variable_expand(node.command)
          final_args = (args + @command_node_args_stack).flatten.map(&:shellescape)
          expanded_args = final_args
          command = CommandFactory.build_command_for(
            world: world,
            command: cmd2execute,
            args:    expanded_args,
            heredoc: (node.heredoc && node.heredoc.value),
            internally_evaluate: node.internally_evaluate?,
            line: @input)
          @stdin, @stdout, @stderr = stream_redirections_for(node)
          set_last_result @blk.call command, @stdin, @stdout, @stderr, pipeline_stack.empty?
          @command_node_args_stack.clear
        end
      end
    end