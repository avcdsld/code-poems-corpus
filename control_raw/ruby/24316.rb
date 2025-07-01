def on_output_change(obj=nil, &block)
      @on_output_change_obj = obj
      @on_output_change = Proc.new { |device, obj_ptr, index, state|
        yield self, @outputs[index], (state == 0 ? false : true), object_for(obj_ptr)
      }
      Klass.set_OnOutputChange_Handler(@handle, @on_output_change, pointer_for(obj))
    end