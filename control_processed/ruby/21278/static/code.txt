def parse_custom_id_from(flow)
      custom_id = flow.id
      if custom_id
        unless custom_id.is_a?(String) || custom_id.is_a?(Integer)
          raise InvalidArgumentError,
                'Provided ID must be a string or an integer'
        end
        custom_id = custom_id.to_s
        if custom_id.length > MAX_ID_SIZE
          raise InvalidArgumentError,
                "Provided Id must not exceed #{MAX_ID_SIZE} bytes"
        end
      end
      custom_id
    end