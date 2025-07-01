def format(win)
      win.win.attron(nc)
      yield
      win.win.attroff(nc)
    end