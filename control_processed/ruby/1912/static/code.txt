def accepted_vpc_peering_connections(options = {})
      batches = Enumerator.new do |y|
        options = Aws::Util.deep_merge(options, filters: [{
          name: "accepter-vpc-info.vpc-id",
          values: [@id]
        }])
        resp = @client.describe_vpc_peering_connections(options)
        resp.each_page do |page|
          batch = []
          page.data.vpc_peering_connections.each do |v|
            batch << VpcPeeringConnection.new(
              id: v.vpc_peering_connection_id,
              data: v,
              client: @client
            )
          end
          y.yield(batch)
        end
      end
      VpcPeeringConnection::Collection.new(batches)
    end