def on_position_change(obj=nil, &block)
	
      @on_position_change_obj = obj
      @on_position_change = Proc.new { |device, obj_ptr, encoder, time, position|
	    yield self, @encoders[encoder], time, position, object_for(obj_ptr)

	}
      Klass.set_OnEncoderPositionChange_Handler(@handle, @on_position_change, pointer_for(obj))
    end