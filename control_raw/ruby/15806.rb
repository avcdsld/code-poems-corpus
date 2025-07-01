def apply_utc_offset( time )
    return time if utc_offset.nil?

    time = time.dup
    if utc_offset == 0
      time.utc
    else
      time.localtime(utc_offset)
    end
    time
  end