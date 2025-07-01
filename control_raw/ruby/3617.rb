def data=(values=[])
      @tag_name = values.first.is_a?(Cell) ? :strCache : :strLit
      values.each do |value|
        v = value.is_a?(Cell) ? value.value : value
        @pt << @type.new(:v => v)
      end
    end