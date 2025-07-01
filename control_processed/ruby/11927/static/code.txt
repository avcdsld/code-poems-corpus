def load_notification_index(target, index_content, options = {})
        case index_content
        when :simple                   then target.notification_index(options)
        when :unopened_simple          then target.unopened_notification_index(options)
        when :opened_simple            then target.opened_notification_index(options)
        when :with_attributes          then target.notification_index_with_attributes(options)
        when :unopened_with_attributes then target.unopened_notification_index_with_attributes(options)
        when :opened_with_attributes   then target.opened_notification_index_with_attributes(options)
        when :none                     then []
        else                                target.notification_index_with_attributes(options)
        end
      end