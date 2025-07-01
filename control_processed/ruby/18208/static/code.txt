def remove_contact(jid)
      bare = JID.new(jid).bare
      @roster.reject! {|c| c.jid.bare == bare }
    end