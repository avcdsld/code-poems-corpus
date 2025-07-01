def stroke_dasharray(*list)
      if list.length.zero?
        primitive 'stroke-dasharray none'
      else
        list.each do |x|
          Kernel.raise ArgumentError, "dash array elements must be > 0 (#{x} given)" if x <= 0
        end
        primitive "stroke-dasharray #{list.join(',')}"
      end
    end