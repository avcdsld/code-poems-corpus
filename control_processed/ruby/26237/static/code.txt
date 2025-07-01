def attr_configurable_bool *args, &block
      trans = attr_configurable_wrap lambda { |v|
        [true, 'true', '1', 1].include?(v) }, block
      attr_configurable_single(*args, &trans)
      args.each do |a|
        unless a.is_a?(Hash)
          alias_method :"#{a}?", a
        end
      end
    end