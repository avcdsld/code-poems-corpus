def classname_list(p)
      classes = []
      while cls = p.hw.ident_chain
        classes << cls
      end
      classes
    end