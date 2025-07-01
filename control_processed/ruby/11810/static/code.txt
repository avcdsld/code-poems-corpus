def define_cmp_method
      keys = @keys
      define_method(:cmp?) do |comparator, other|
        keys.all? do |key|
          __send__(key).public_send(comparator, other.__send__(key))
        end
      end
      private :cmp?
    end