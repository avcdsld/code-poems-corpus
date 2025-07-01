def as_json(pretty=false)

      pretty ? Rufus::Json.pretty_encode(@h) : Rufus::Json.encode(@h)
    end