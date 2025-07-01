def ref=(cell_reference)
      cell_reference = cell_reference.r if cell_reference.is_a?(Cell)
      Axlsx::validate_string cell_reference
      @ref = cell_reference
    end