def versions(options = {})
      batches = Enumerator.new do |y|
        options = options.merge(policy_arn: @arn)
        resp = @client.list_policy_versions(options)
        resp.each_page do |page|
          batch = []
          page.data.versions.each do |v|
            batch << PolicyVersion.new(
              arn: @arn,
              version_id: v.version_id,
              data: v,
              client: @client
            )
          end
          y.yield(batch)
        end
      end
      PolicyVersion::Collection.new(batches)
    end