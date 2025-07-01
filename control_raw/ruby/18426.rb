def link_list(expand_size)
      list = [@base]
      # fd
      work = proc do |ptr, nxt, append|
        sz = 0
        dup = {}
        while ptr != @base && sz < expand_size
          append.call(ptr)
          break if ptr.nil? || dup[ptr] # invalid or duplicated pointer

          dup[ptr] = true
          ptr = __send__(nxt, ptr)
          sz += 1
        end
      end
      work.call(@fd, :fd_of, ->(ptr) { list << ptr })
      work.call(@bk, :bk_of, ->(ptr) { list.unshift(ptr) })
      list
    end