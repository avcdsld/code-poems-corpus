def write_asset_file(directory, asset)
      FileUtils.mkpath(directory) unless File.directory?(directory)
      begin
        # Save file to disk
        File.open(File.join(directory, asset.filename), 'w') do |file|
          file.write(asset.content)
        end
      rescue StandardError => se
        puts "Asset Pipeline: Failed to save '#{asset.filename}' to " \
             "disk: #{se.message}"
        raise se
      end
    end