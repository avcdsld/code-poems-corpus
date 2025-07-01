def function_properties
      properties = @task.properties
      if @task.build_function_iam?
        iam_policy = Jets::Resource::Iam::FunctionRole.new(@task)
        properties[:role] = "!GetAtt #{iam_policy.logical_id}.Arn"
      end
      properties
    end