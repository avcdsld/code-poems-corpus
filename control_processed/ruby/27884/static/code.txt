def _configure s
      s[:row] ||= 0
      s[:col] ||= 0
      s[:row] += (s[:margin_top] || 0)
      s[:col] += (s[:margin_left] || 0)
      s[:width] = FFI::NCurses.COLS-s[:col] if s[:width] == :expand
      s[:height] = FFI::NCurses.LINES-s[:row] if s[:height] == :expand # 2011-11-30 
      last = @_ws_active.last
      if last
        if s[:width_pc]
          if last.is_a? WsStack
            s[:width] =           (last[:width] * (s[:width_pc].to_i * 0.01)).floor
          else
            # i think this width is picked up by next stack in this flow
            last[:item_width] =   (last[:width] * (s[:width_pc].to_i* 0.01)).floor
          end
        end
        if s[:height_pc]
          if last.is_a? WsFlow
            s[:height] =       ( (last[:height] * s[:height_pc].to_i)/100).floor
          else
            # this works only for flows within stacks not for an object unless
            # you put a single object in a flow
            s[:item_height] =  ( (last[:height] * s[:height_pc].to_i)/100).floor
          end
            #alert "item height set as #{s[:height]} for #{s} "
        end
        if last.is_a? WsStack
          s[:row] += (last[:row] || 0)
          s[:col] += (last[:col] || 0)  
        else
          s[:row] += (last[:row] || 0)
          s[:col] += (last[:col] || 0)  # we are updating with item_width as each st finishes
          s[:width] ||= last[:item_width] # 
        end
      else
        # this should be outer most flow or stack, if nothing mentioned
        # trying this out
        s[:width] ||= :expand
        s[:height] ||= :expand
        s[:width] = FFI::NCurses.COLS-s[:col] if s[:width] == :expand
        s[:height] = FFI::NCurses.LINES-s[:row] if s[:height] == :expand # 2011-11-30 
      end
      s[:components] = []
    end