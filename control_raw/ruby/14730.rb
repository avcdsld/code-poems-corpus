def initialize_states(object, options = {}, attributes = {})
      options.assert_valid_keys( :static, :dynamic, :to)
      options = {:static => true, :dynamic => true}.merge(options)

      result = yield if block_given?

      each_value do |machine|
        unless machine.dynamic_initial_state?
          force = options[:static] == :force || !attributes.keys.map(&:to_sym).include?(machine.attribute)
          machine.initialize_state(object, force: force, :to => options[:to])
        end
      end if options[:static]

      each_value do |machine|
        machine.initialize_state(object, :force => options[:dynamic] == :force, :to => options[:to]) if machine.dynamic_initial_state?
      end if options[:dynamic]

      result
    end