def composite overlay, mode, opts = {}
      unless overlay.is_a? Array
        overlay = [overlay]
      end
      unless mode.is_a? Array
        mode = [mode]
      end

      mode = mode.map do |x|
        GObject::GValue.from_nick Vips::BLEND_MODE_TYPE, x
      end

      Vips::Image.composite([self] + overlay, mode, opts)
    end