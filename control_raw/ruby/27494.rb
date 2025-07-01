def screenshot(width, height, quality)
      url = player_url+'/application/screenshot?'
      url += "width=#{width}"
      url += "&height=#{height}"
      url += "&quality=#{quality}"

      ping url
    end