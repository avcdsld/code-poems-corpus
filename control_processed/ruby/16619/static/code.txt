def retrlines(cmd) # :yield: line
      synchronize do
	with_binary(false) do
          conn = transfercmd(cmd)
          loop do
            line = conn.gets
            break if line == nil
            yield(line.sub(/\r?\n\z/, ""), !line.match(/\n\z/).nil?)
          end
          conn.close
          voidresp
        end
      end
    end