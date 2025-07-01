def to_b
      raise ISO8583Exception.new "no MTI set!" unless mti
      mti_enc = self.class._mti_format.encode(mti)
      mti_enc << _body.join
    end