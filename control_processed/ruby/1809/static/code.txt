def create_route_table(options = {})
      resp = @client.create_route_table(options)
      RouteTable.new(
        id: resp.data.route_table.route_table_id,
        data: resp.data.route_table,
        client: @client
      )
    end