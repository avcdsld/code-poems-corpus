def policies(options = {})
      batches = Enumerator.new do |y|
        options = options.merge(role_name: @name)
        resp = @client.list_role_policies(options)
        resp.each_page do |page|
          batch = []
          page.data.policy_names.each do |p|
            batch << RolePolicy.new(
              role_name: @name,
              name: p,
              client: @client
            )
          end
          y.yield(batch)
        end
      end
      RolePolicy::Collection.new(batches)
    end