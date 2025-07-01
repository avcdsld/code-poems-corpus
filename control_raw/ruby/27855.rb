def default_string_key_map
      require 'canis/core/include/action'
      @key_map ||= {}
      @key_map[ Regexp.new('[a-zA-Z0-9_\.\/]') ] = Action.new("Append to pattern") { |obj, ch|
        obj.buffer << ch.chr
        obj.buffer_changed
      }
      @key_map[ [127, ?\C-h.getbyte(0)] ] = Action.new("Delete Prev Char") { |obj, ch|
        # backspace
        buff = obj.buffer
        buff = buff[0..-2] unless buff == ""
        obj.set_buffer buff
      }
    end