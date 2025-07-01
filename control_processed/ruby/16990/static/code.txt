def condition_fulfilled?(model, condition, options)
      case condition
      when Symbol
        result = model.send(condition)
      when Proc
        result = call_proc(condition, model, options)
      end
      !!result
    end