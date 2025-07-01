def interpreted_data
      if d = pushdata
        return d
      end
      opcode = self.opcode
      if opcode == OP_1NEGATE || (opcode >= OP_1 && opcode <= OP_16)
        ScriptNumber.new(integer: opcode - OP_1 + 1).data
      else
        nil
      end
    end