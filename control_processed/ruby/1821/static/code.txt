def internet_gateways(options = {})
      batches = Enumerator.new do |y|
        resp = @client.describe_internet_gateways(options)
        resp.each_page do |page|
          batch = []
          page.data.internet_gateways.each do |i|
            batch << InternetGateway.new(
              id: i.internet_gateway_id,
              data: i,
              client: @client
            )
          end
          y.yield(batch)
        end
      end
      InternetGateway::Collection.new(batches)
    end