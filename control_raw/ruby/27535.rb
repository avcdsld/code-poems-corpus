def create_class(name, options={})
      raise ArgumentError, "class name is blank" if blank?(name)
      opt_pattern = {
          :extends => :optional, :cluster => :optional, :force => false, :abstract => false,
          :properties => :optional
      }
      verify_options(options, opt_pattern)

      sql = "CREATE CLASS #{name}"
      sql << " EXTENDS #{options[:extends]}" if options.include? :extends
      sql << " CLUSTER #{options[:cluster]}" if options.include? :cluster
      sql << ' ABSTRACT' if options.include?(:abstract)

      drop_class name if options[:force]

      command sql

      # properties given?
      if options.include? :properties
        props = options[:properties]
        raise ArgumentError, 'properties have to be an array' unless props.is_a? Array

        props.each do |prop|
          raise ArgumentError, 'property definition has to be a hash' unless prop.is_a? Hash
          prop_name = prop.delete :property
          prop_type = prop.delete :type
          create_property(name, prop_name, prop_type, prop)
        end
      end

      if block_given?
        proxy = Orientdb4r::Utils::Proxy.new(self, name)
        def proxy.property(property, type, options={})
          self.target.send :create_property, self.context, property, type, options
        end
        def proxy.link(property, type, linked_class, options={})
          raise ArgumentError, "type has to be a linked-type, given=#{type}" unless type.to_s.start_with? 'link'
          options[:linked_class] = linked_class
          self.target.send :create_property, self.context, property, type, options
        end
        yield proxy
      end
    end