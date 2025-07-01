def run_authorization_check
      if instance_authority_resource.is_a?(Array)
        # Array includes options; pass as separate args
        authorize_action_for(*instance_authority_resource, *authority_arguments)
      else
        # *resource would be interpreted as resource.to_a, which is wrong and
        # actually triggers a query if it's a Sequel model
        authorize_action_for(instance_authority_resource, *authority_arguments)
      end
    end