def list(user_role)
      response = get_request("/2.0/teams/?role=#{user_role.to_s}")
      return response["values"] unless block_given?
      response["values"].each { |el| yield el }
    end