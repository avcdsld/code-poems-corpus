def apply_to_method(method)
      filtered_advices = filter_advices advices, method
      return if filtered_advices.empty?

      logger.debug 'apply-to-method', method

      scope ||= context.instance_method_type(method)

      recreate_method method, filtered_advices, scope
    end