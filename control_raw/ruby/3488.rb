def handle_value_definition
      value_def = @entry.at_xpath('./*/cda:repeatNumber', HQMF2::Document::NAMESPACES)
      unless value_def
        # TODO: HQMF needs better differentiation between SUM & COUNT...
        # currently using presence of repeatNumber...
        @type = 'SUM' if @type == 'COUNT'
        value_def = @entry.at_xpath('./*/cda:value', HQMF2::Document::NAMESPACES)
      end

      # TODO: Resolve extracting values embedded in criteria within outboundRel's
      if @type == 'SUM'
        value_def = @entry.at_xpath('./*/*/*/cda:value', HQMF2::Document::NAMESPACES)
      end

      if value_def
        value_type = value_def.at_xpath('./@xsi:type', HQMF2::Document::NAMESPACES)
        @value = HQMF2::AnyValue.new if String.try_convert(value_type) == 'ANY'
      end

      value_def
    end