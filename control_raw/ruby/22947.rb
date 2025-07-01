def to_risc( compiler )
      name_ = @name
      cache_entry_ = @cache_entry
      builder = compiler.builder(self)
      builder.build do
        word! << name_
        cache_entry! << cache_entry_

        type! << cache_entry[:cached_type]
        callable_method! << type[:methods]

        add_code while_start_label

        object! << Parfait.object_space.nil_object
        object - callable_method
        if_zero exit_label

        name! << callable_method[:name]
        name - word

        if_zero ok_label

        callable_method << callable_method[:next_callable]
        branch  while_start_label

        add_code exit_label
        # temporary, need to raise really.
        factory! << Parfait.object_space.get_factory_for(:Integer)
        integer_tmp! << factory[:reserve]
        Risc::Builtin::Object.emit_syscall( builder , :exit ) #uses integer_tmp

        add_code ok_label
        cache_entry[:cached_method] << callable_method
      end
    end