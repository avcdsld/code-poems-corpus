def auths
      json = client.get("/v1/sys/auth")
      json = json[:data] if json[:data]
      return Hash[*json.map do |k,v|
        [k.to_s.chomp("/").to_sym, Auth.decode(v)]
      end.flatten]
    end