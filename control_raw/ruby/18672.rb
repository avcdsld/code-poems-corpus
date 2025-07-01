def truncate(str, length, options = {})
      text = str.dup
      options[:omission] ||= "..."

      length_with_room_for_omission = length - options[:omission].length
      stop = options[:separator] ?
        (text.rindex(options[:separator], length_with_room_for_omission) || length_with_room_for_omission) : length_with_room_for_omission

      (text.length > length ? text[0...stop] + options[:omission] : text).to_s
    end