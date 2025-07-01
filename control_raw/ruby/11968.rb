def notification_targets(target_type, options = {})
      target_typed_method_name = "notification_#{cast_to_resources_name(target_type)}"
      resolved_parameter = resolve_parameter(
        target_typed_method_name,
        _notification_targets[cast_to_resources_sym(target_type)],
        nil,
        options)
      unless resolved_parameter
        raise NotImplementedError, "You have to implement #{self.class}##{target_typed_method_name} "\
                                   "or set :targets in acts_as_notifiable"
      end
      resolved_parameter
    end