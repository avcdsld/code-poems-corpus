def render_data pad, lineno, text
        text = text.join
        # FIXME why repeatedly getting this colorpair
        cp = @color_pair
        att = @attrib
        # added for selection, but will crash if selection is not extended !!! XXX
          if @source.is_row_selected? lineno
            att = REVERSE
            # FIXME currentl this overflows into next row
          end

        FFI::NCurses.wattron(pad,FFI::NCurses.COLOR_PAIR(cp) | att)
        FFI::NCurses.mvwaddstr(pad, lineno, 0, text)
        FFI::NCurses.wattroff(pad,FFI::NCurses.COLOR_PAIR(cp) | att)
      end