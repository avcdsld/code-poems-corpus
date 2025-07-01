def colorize_count(str, count, colorize_method)
      str= str % [count]
      str= Colorize.send(colorize_method, str) if colorize_method and count != 0
      str
    end