def jwts
      apps = []
      response = client.get("#{@api_end_point}#{self.id}/jwt") rescue nil
      if response
        response['data'].each do |attributes|
          apps << Kong::JWT.new(attributes)
        end
      end
      apps
    end