def load_from_id(gid)
      @gid = gid
      @xml_data = GamedayFetcher.fetch_eventlog(gid)
      @xml_doc = REXML::Document.new(@xml_data)
      if @xml_doc.root
        set_teams
        set_events
      end
    end