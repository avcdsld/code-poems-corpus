def versions(options = {})
      batches = Enumerator.new do |y|
        options = options.merge(engine: @name)
        resp = @client.describe_db_engine_versions(options)
        resp.each_page do |page|
          batch = []
          page.data.db_engine_versions.each do |d|
            batch << DBEngineVersion.new(
              engine_name: @name,
              version: d.engine_version,
              data: d,
              client: @client
            )
          end
          y.yield(batch)
        end
      end
      DBEngineVersion::Collection.new(batches)
    end