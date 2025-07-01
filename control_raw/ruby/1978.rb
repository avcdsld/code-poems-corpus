def run_callback(method, *args)
      case method
      when Symbol
        send(method, *args)
      when Proc
        instance_exec(*args, &method)
      else
        raise "Please register with callbacks using a symbol or a block/proc."
      end
    end