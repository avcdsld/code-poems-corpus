def order_id=(order_id)

      if !order_id.nil? && order_id.to_s.length > 192
        fail ArgumentError, "invalid value for 'order_id', the character length must be smaller than or equal to 192."
      end

      @order_id = order_id
    end