def double_tap(query, options={})
      ensure_query_class_or_nil(query)

      gesture_options = options.dup
      gesture_options[:at] ||= {}
      gesture_options[:at][:x] ||= 50
      gesture_options[:at][:y] ||= 50
      gesture_options[:timeout] ||= Calabash::Gestures::DEFAULT_GESTURE_WAIT_TIMEOUT

      _double_tap(query, gesture_options)
    end