def bind
      Spinach.hooks.tap do |hooks|
        hooks.before_run { |*args| before_run(*args) }
        hooks.after_run { |*args| after_run(*args) }
        hooks.before_feature { |*args| before_feature_run(*args) }
        hooks.after_feature { |*args| after_feature_run(*args) }
        hooks.on_undefined_feature { |*args| on_feature_not_found(*args) }
        hooks.before_scenario { |*args| before_scenario_run(*args) }
        hooks.around_scenario { |*args, &block| around_scenario_run(*args, &block) }
        hooks.after_scenario { |*args| after_scenario_run(*args) }
        hooks.on_successful_step { |*args| on_successful_step(*args) }
        hooks.on_undefined_step { |*args| on_undefined_step(*args) }
        hooks.on_pending_step { |*args| on_pending_step(*args) }
        hooks.on_failed_step { |*args| on_failed_step(*args) }
        hooks.on_error_step { |*args| on_error_step(*args) }
        hooks.on_skipped_step { |*args| on_skipped_step(*args) }

        hooks.before_feature { |*args| set_current_feature(*args) }
        hooks.after_feature { |*args| clear_current_feature(*args) }
        hooks.before_scenario { |*args| set_current_scenario(args.first) }
        hooks.after_scenario { |*args| clear_current_scenario(args.first) }
      end
    end