def followers(team_name)
      response = get_request("/2.0/teams/#{team_name.to_s}/followers")
      return response["values"] unless block_given?
      response["values"].each { |el| yield el }
    end