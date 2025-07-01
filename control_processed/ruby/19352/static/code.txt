def list_users
      r = execute(make_xml('UserListingRequest'))
      arr = []
      if r.success
        r.res.elements.each('UserListingResponse/UserSummary') do |summary|
          arr << UserSummary.parse(summary)
        end
      end
      arr
    end