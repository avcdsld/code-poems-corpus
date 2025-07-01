def cascadable_child?(kind, child, association)
      return false if kind == :initialize || kind == :find || kind == :touch
      return false if kind == :validate && association.validate?
      child.callback_executable?(kind) ? child.in_callback_state?(kind) : false
    end