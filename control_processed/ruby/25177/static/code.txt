def add_border(cell_ref, args = :all)
      cells = self[cell_ref]
      BorderCreator.new(self, cells, args).draw
    end