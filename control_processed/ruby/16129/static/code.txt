def messages_count(user)
      Message.search do
        with(:receiver_id).equal_to user.id
        with(:is_read).equal_to false
      end.hits.total_entries
    end