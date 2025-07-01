def read_binary_object_at(fname,fd,pos)
      position = @offsets[pos]
      fd.seek(position,IO::SEEK_SET)
      read_binary_object(fname,fd)
    end