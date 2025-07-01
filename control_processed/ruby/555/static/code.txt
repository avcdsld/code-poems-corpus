def upload_metadata
      upload_metadata = UploadMetadata.new
      upload_screenshots = UploadScreenshots.new

      # First, collect all the things for the HTML Report
      screenshots = upload_screenshots.collect_screenshots(options)
      upload_metadata.load_from_filesystem(options)

      # Assign "default" values to all languages
      upload_metadata.assign_defaults(options)

      # Handle app icon / watch icon
      prepare_app_icons(options)

      # Validate
      validate_html(screenshots)

      # Commit
      upload_metadata.upload(options)
      upload_screenshots.upload(options, screenshots)
      UploadPriceTier.new.upload(options)
      UploadAssets.new.upload(options) # e.g. app icon
    end