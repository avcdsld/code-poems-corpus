def serialize_old_format
      buf = [version].pack('V')
      buf << Bitcoin.pack_var_int(inputs.length) << inputs.map(&:to_payload).join
      buf << Bitcoin.pack_var_int(outputs.length) << outputs.map(&:to_payload).join
      buf << [lock_time].pack('V')
      buf
    end