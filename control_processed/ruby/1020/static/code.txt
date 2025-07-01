def store_dir
      default_path = "uploads/#{model.class.to_s.underscore}/#{mounted_as}/#{model.id}"

      return File.join(Decidim.base_uploads_path, default_path) if Decidim.base_uploads_path.present?
      default_path
    end