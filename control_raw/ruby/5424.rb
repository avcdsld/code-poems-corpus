def upvote
      begin
        client.post("/cards/#{id}/membersVoted", {
          value: me.id
        })
      rescue Trello::Error => e
        fail e unless e.message =~ /has already voted/i
      end

      self
    end