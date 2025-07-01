def check_condition(condition, caller)
      Watir.logger.debug "<- `Verifying precondition #{inspect}##{condition} for #{caller}`"
      begin
        condition.nil? ? assert_exists : send(condition)
        Watir.logger.debug "<- `Verified precondition #{inspect}##{condition || 'assert_exists'}`"
      rescue unknown_exception
        raise unless condition.nil?

        Watir.logger.debug "<- `Unable to satisfy precondition #{inspect}##{condition}`"
        check_condition(:wait_for_exists, caller)
      end
    end