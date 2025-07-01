def non_object_image
      image = list_item.image

      return image.file.url if image.respond_to?(:file)
      return image if image.present?

      fallback_image
    end