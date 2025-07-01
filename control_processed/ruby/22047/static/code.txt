def transcript(transcript_date = Date.today)
      url = "/room/#{@id}/transcript/#{transcript_date.strftime('%Y/%m/%d')}.json"
      connection.get(url)['messages'].map do |message|
        parse_message(message)
      end
    end