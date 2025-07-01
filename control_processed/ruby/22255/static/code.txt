def preview_image(size = :small)
      preview_image = object&.preview_image&.url(size)
      return preview_image if preview_image.present?

      image(size, false)
    end