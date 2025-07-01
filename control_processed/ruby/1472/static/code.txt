def policies(options = {})
      batches = Enumerator.new do |y|
        options = options.merge(group_name: @name)
        resp = @client.list_group_policies(options)
        resp.each_page do |page|
          batch = []
          page.data.policy_names.each do |p|
            batch << GroupPolicy.new(
              group_name: @name,
              name: p,
              client: @client
            )
          end
          y.yield(batch)
        end
      end
      GroupPolicy::Collection.new(batches)
    end