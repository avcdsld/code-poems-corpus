def first_set
      @first_set ||= Racc.set_closure([self]) do |sym|
        sym.heads.each_with_object([]) do |ptr, next_syms|
          while !ptr.reduce?
            next_syms << ptr.symbol
            ptr.symbol.nullable? ? ptr = ptr.next : break
          end
        end
      end.freeze
    end