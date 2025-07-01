def validate_fields
      l = Block.serialize self
      RLP.decode(RLP.encode(l)) == l
    end