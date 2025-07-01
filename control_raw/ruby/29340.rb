def handle_input(*input)
      while ch = next_ch(input)
        quit  = QUIT_CONTROLS.include?(ch)
        enter = ENTER_CONTROLS.include?(ch)
        inc   = INC_CONTROLS.include?(ch)
        dec   = DEC_CONTROLS.include?(ch)

        break if shutdown? ||
                (quit && (!enter || quit_on_enter?))

        if enter
          on_enter

        elsif inc
          on_inc

        elsif dec
          on_dec
        end

        if key_bound?(ch)
          invoke_key_bindings(ch)
        end

        on_key(ch)
      end

      ch
    end