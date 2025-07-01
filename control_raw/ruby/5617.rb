def to_a
      @control.all_cookies.map do |e|
        e.merge(expires: e[:expires] ? e[:expires].to_time : nil)
      end
    end