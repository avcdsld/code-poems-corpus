def add_remote_repository( url, username = nil, password = nil )
      if username
        @resolver.addRemoteRepositoryByUrl( url, username, password )
      else
        @resolver.addRemoteRepositoryByUrl( url )
      end
    end