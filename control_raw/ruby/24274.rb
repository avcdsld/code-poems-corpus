def on_server_connect(obj=nil, &block)
      @on_server_connect_obj = obj
      @on_server_connect = Proc.new { |handle, obj_ptr|
        yield self, object_for(obj_pointer)
      }
      Klass.set_OnServerConnect_Handler(@handle, @on_server_connect, pointer_for(obj))
    end