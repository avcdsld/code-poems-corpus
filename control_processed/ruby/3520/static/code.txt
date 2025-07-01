def extract_derivation_operator
      codes = @entry.xpath("./*/cda:outboundRelationship[@typeCode='COMP']/cda:conjunctionCode/@code",
                           HQMF2::Document::NAMESPACES)
      codes.inject(nil) do |d_op, code|
        if d_op && d_op != CONJUNCTION_CODE_TO_DERIVATION_OP[code.value]
          fail 'More than one derivation operator in data criteria'
        end
        CONJUNCTION_CODE_TO_DERIVATION_OP[code.value]
      end
    end