def create_member(data)
      headers = @client.make_request(:post, @client.concat_user_path("#{CONFERENCE_PATH}/#{id}/members"), data)[1]
      id = Client.get_id_from_location_header(headers[:location])
      get_member(id)
    end