def move_on(workitem=h.applied_workitem)

      position = workitem['fei'] == h.fei ?
        -1 : Ruote::FlowExpressionId.child_id(workitem['fei'])

      position += 1

      com, arg = get_command(workitem)

      return reply_to_parent(workitem) if com == 'break'

      case com
        when 'rewind', 'continue', 'reset' then position = 0
        when 'skip' then position += arg
        when 'jump' then position = jump_to(workitem, position, arg)
      end

      position = 0 if position >= tree_children.size && is_loop?

      if position < tree_children.size

        workitem = h.applied_workitem if com == 'reset'
        apply_child(position, workitem)

      else

        reply_to_parent(workitem)
      end
    end