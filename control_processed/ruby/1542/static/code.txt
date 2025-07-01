def snapshots(options = {})
      batches = Enumerator.new do |y|
        options = options.merge(db_instance_identifier: @id)
        resp = @client.describe_db_snapshots(options)
        resp.each_page do |page|
          batch = []
          page.data.db_snapshots.each do |d|
            batch << DBSnapshot.new(
              instance_id: options[:db_instance_identifier],
              snapshot_id: d.db_snapshot_identifier,
              data: d,
              client: @client
            )
          end
          y.yield(batch)
        end
      end
      DBSnapshot::Collection.new(batches)
    end