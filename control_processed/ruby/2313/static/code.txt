def save
      n_cmds = Setting[:histsize] > size ? size : Setting[:histsize]

      File.open(Setting[:histfile], "w") do |file|
        n_cmds.times { file.puts(pop) }
      end

      clear
    end