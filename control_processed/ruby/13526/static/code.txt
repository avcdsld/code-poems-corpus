def notifications(ast)
      # Sanity check the AST provided.
      return [] unless ast.respond_to?(:xpath)

      # We are mapping each `notifies` or `subscribes` line in the provided
      # AST to a Hash with the extracted details.
      notification_nodes(ast).map do |notify|

        # Chef supports two styles of notification.
        notified_resource = if new_style_notification?(notify)
                              # `notifies :restart, "service[foo]"`
                              new_style_notification(notify)
                            else
                              # `notifies :restart, resources(service: "foo")`
                              old_style_notification(notify)
                            end

        # Ignore if the notification was not parsed
        next unless notified_resource

        # Now merge the extract notification details with the attributes
        # that are common to both styles of notification.
        notified_resource.merge(
          {
            # The `:type` of notification: `:subscribes` or `:notifies`.
            type: notification_type(notify),

            # The `:style` of notification: `:new` or `:old`.
            style: new_style_notification?(notify) ? :new : :old,

            # The target resource action.
            action: notification_action(notify),

            # The notification timing: `:before`, `:immediate` or `:delayed`.
            timing: notification_timing(notify),
          }
        )
      end.compact
    end