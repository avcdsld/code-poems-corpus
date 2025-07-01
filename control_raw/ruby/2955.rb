def radio_button(name, identifier={:index => 0}, &block)
      standard_methods(name, identifier, 'radio_button_for', &block)
      define_method("select_#{name}") do
        return platform.select_radio(identifier.clone) unless block_given?
        self.send("#{name}_element").select
      end
      define_method("#{name}_selected?") do
        return platform.radio_selected?(identifier.clone) unless block_given?
        self.send("#{name}_element").selected?
      end
    end