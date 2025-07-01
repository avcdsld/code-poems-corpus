def module_methods_in(klass)
      klass.included_modules.each_with_object([]) do |mod, accumulator|
        if mod.to_s =~ /#{klass}/
          mod.instance_methods(false).each do |method|
            accumulator << method
          end
        end
        accumulator
      end
    end