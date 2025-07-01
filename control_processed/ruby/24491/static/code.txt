def size_of frame_type
      detection = "is_#{frame_type.to_s.sub(/frames$/, 'frame')}?"
      @meta.select { |m|
        Frame.new(nil, m[:id], m[:flag]).send detection
      }.size
    end