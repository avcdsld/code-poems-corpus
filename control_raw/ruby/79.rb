def find(dirs)
      dirs.inject({}) { |h, dir| h.update(find_in(dir)) }
    end