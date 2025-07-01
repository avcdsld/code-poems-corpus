def publish_to_optional_targets(options = {})
      notifiable.optional_targets(target.to_resources_name, key).map { |optional_target|
        optional_target_name = optional_target.to_optional_target_name
        if optional_target_subscribed?(optional_target_name)
          optional_target.notify(self, options[optional_target_name] || {})
          [optional_target_name, true]
        else
          [optional_target_name, false]
        end
      }.to_h
    end