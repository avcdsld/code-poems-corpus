def radio_input choice, options = {}, &block
      fieldset_attribute = self.current_fieldset_attribute

      panel = if block_given? || options.key?(:panel_id)
        panel_id = options.delete(:panel_id) { [fieldset_attribute, choice, 'panel'].join('_') }
        options.merge!('data-target': panel_id)
        revealing_panel(panel_id, flush: false, &block) if block_given?
      end

      option = radio_inputs(
        fieldset_attribute,
        options.merge(choices: [choice])
      ).first + "\n"

      safe_concat([option, panel].join)
    end