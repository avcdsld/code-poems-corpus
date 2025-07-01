def use_board!(boardname)
      return true if use_board(boardname)

      boardfamily = boardname.split(":")[0..1].join(":")
      puts "Board '#{boardname}' not found; attempting to install '#{boardfamily}'"
      return false unless install_boards(boardfamily) # guess board family from first 2 :-separated fields

      use_board(boardname)
    end