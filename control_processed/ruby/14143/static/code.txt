def insert_field(order,field = {})
      field_ok? field
      @fields.insert((order -1), field)
      order_fields
      @need_to_update = true
    end