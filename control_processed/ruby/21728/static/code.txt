def frame=(value)
      selected.each do |view|
        RubyMotionQuery::Rect.update_view_frame(view, value)
      end
    end