def plan(action_class, targets, *args)
      check_targets!(targets)
      plan_self(:action_class => action_class.to_s,
                :target_ids => targets.map(&:id),
                :target_class => targets.first.class.to_s,
                :args => args)
    end