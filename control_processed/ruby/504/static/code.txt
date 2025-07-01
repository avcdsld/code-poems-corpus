def installed_identities
      available = request_valid_identities
      ids = {}
      available.split("\n").each do |current|
        begin
          sha1 = current.match(/[a-zA-Z0-9]{40}/).to_s
          name = current.match(/.*\"(.*)\"/)[1]
          ids[sha1] = name
        rescue
          nil
        end # the last line does not match
      end

      ids
    end