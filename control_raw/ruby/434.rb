def write_metadata
      unless disabled?
        Jekyll.logger.debug "Writing Metadata:", ".jekyll-metadata"
        File.binwrite(metadata_file, Marshal.dump(metadata))
      end
    end