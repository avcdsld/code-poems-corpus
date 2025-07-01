def info
      response = connection.get("/playback-info").response
      plist = CFPropertyList::List.new(data: response.body)
      hash = CFPropertyList.native_types(plist.value)
      PlaybackInfo.new(hash)
    end