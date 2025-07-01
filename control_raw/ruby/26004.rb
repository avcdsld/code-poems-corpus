def find_container(host)
      id = host['docker_container_id']
      name = host['docker_container_name']
      return unless id || name

      containers = ::Docker::Container.all

      if id
        @logger.debug("Looking for an existing container with ID #{id}")
        container = containers.select { |c| c.id == id }.first
      end

      if name && container.nil?
        @logger.debug("Looking for an existing container with name #{name}")
        container = containers.select do |c|
          c.info['Names'].include? "/#{name}"
        end.first
      end

      return container unless container.nil?
      @logger.debug("Existing container not found")
    end