def define_calculated_statistic(name, &block)
      method_name = name.to_s.gsub(" ", "").underscore + "_stat"

      @statistics ||= {}
      @statistics[name] = method_name

      (class<<self; self; end).instance_eval do
        define_method(method_name) do |filters|
          @filters = filters
          yield
        end
      end
    end