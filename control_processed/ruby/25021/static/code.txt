def remove
      with_retry(cluster) do
        cluster.with_primary do |node|
          node.remove(
            operation.database,
            operation.collection,
            operation.basic_selector,
            write_concern,
            flags: [ :remove_first ]
          )
        end
      end
    end