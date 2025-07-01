def ecs_deploy(id, &block)
      service = Aws::Ecs.services(ecs_cluster_name, [resource(id)]).first
      taskdef = get_taskdef(service)

      ## convert to a hash and modify in block
      hash = taskdef_to_hash(taskdef)
      yield(hash) if block_given?

      taskdef = register_taskdef(hash)
      update_service(service, taskdef)
    end