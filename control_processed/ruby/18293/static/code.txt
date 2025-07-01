def type_id=(id)
      type_id = id.to_i

      raise InvalidShippingTypeError,
        "invalid #{id.inspect} type id" unless TYPE.value?(type_id)

      @type_id = type_id
      @type_name = TYPE.key(type_id)
    end