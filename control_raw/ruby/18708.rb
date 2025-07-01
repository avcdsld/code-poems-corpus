def param(name, transform: nil)
      if @command.explicitly_no_params?
        raise AlreadySpecifiedAsNoParams.new(name, @command)
      end

      @command.parameter_definitions << Cri::ParamDefinition.new(
        name: name,
        transform: transform,
      )
    end