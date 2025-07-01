def add_tags
      @hosts.each do |host|
        instance = host['instance']

        # Define tags for the instance
        @logger.notify("aws-sdk: Add tags for #{host.name}")

        tags = [
          {
            :key   => 'jenkins_build_url',
            :value => @options[:jenkins_build_url],
          },
          {
            :key   => 'Name',
            :value => host.name,
          },
          {
            :key   => 'department',
            :value => @options[:department],
          },
          {
            :key   => 'project',
            :value => @options[:project],
          },
          {
            :key   => 'created_by',
            :value => @options[:created_by],
          },
        ]

        host[:host_tags].each do |name, val|
          tags << { :key => name.to_s, :value => val }
        end

        client.create_tags(
          :resources => [instance.instance_id],
          :tags      => tags.reject { |r| r[:value].nil? },
        )
      end

      nil
    end