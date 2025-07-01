def generate_deliver_file(deliver_path, options)
      v = options[:app].latest_version
      metadata_path = options[:metadata_path] || File.join(deliver_path, 'metadata')
      generate_metadata_files(v, metadata_path)

      # Generate the final Deliverfile here
      return File.read(deliverfile_path)
    end