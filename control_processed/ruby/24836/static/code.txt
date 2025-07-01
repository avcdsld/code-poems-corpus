def open
      @fd.close if @fd
      @fd = File.open(@file, 'ab+')
      @fd.advise(:sequential) if @fd.respond_to? :advise
      stat = @fd.stat
      @inode = stat.ino
      write(@format.header) if stat.size == 0
      @pos = nil
    end