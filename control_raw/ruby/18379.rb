def export(canvas)
      image = Magick::Image.new(canvas.width, canvas.height)
      image.import_pixels(0, 0, canvas.width, canvas.height, "RGBA", canvas.pixels.pack("N*"))
      image
    end