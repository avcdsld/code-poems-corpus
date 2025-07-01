def upsert_agent(instance)
      @logger.info("Adding agent #{instance.agent_id} (#{instance.job}/#{instance.id}) to #{name}...")

      agent_id = instance.agent_id

      if agent_id.nil?
        @logger.warn("No agent id for instance #{instance.job}/#{instance.id} in deployment #{name}")
        #count agents for instances with deleted vm, which expect to have vm
        if instance.expects_vm? && !instance.has_vm?
          agent = Agent.new("agent_with_no_vm", deployment: name)
          @instance_id_to_agent[instance.id] = agent
          agent.update_instance(instance)
        end
        return false
      end

      # Idle VMs, we don't care about them, but we still want to track them
      if instance.job.nil?
        @logger.debug("VM with no job found: #{agent_id}")
      end

      agent = @agent_id_to_agent[agent_id]

      if agent.nil?
        @logger.debug("Discovered agent #{agent_id}")
        agent = Agent.new(agent_id, deployment: name)
        @agent_id_to_agent[agent_id] = agent
        @instance_id_to_agent.delete(instance.id) if @instance_id_to_agent[instance.id]
      end

      agent.update_instance(instance)

      true
    end