def lookup_class_properties(klass)
      all_classes = []
      while klass != Object
        all_classes << klass
        klass = klass.superclass
      end
      class_properties = {}
      # Go back down class heirachry top to down
      all_classes.reverse.each do |k|
        class_properties.merge!(k.class_properties)
      end
      class_properties
    end