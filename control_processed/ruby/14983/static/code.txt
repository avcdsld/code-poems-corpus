def on_command_call(*args)
    if args.last && :args == args.last[0]
      args_add = args.pop
      call = on_call(*args)
      on_method_add_arg(call, args_add)
    else
      super
    end
  end