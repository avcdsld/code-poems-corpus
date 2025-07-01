def cache(package, extension, contents, output_dir, suffix=nil, mtime=nil)
      FileUtils.mkdir_p(output_dir) unless File.exists?(output_dir)
      raise OutputNotWritable, "Jammit doesn't have permission to write to \"#{output_dir}\"" unless File.writable?(output_dir)
      mtime ||= latest_mtime package_for(package, extension.to_sym)[:paths]
      files = []
      files << file_name = File.join(output_dir, Jammit.filename(package, extension, suffix))
      File.open(file_name, 'wb+') {|f| f.write(contents) }
      if Jammit.gzip_assets
        files << zip_name = "#{file_name}.gz"
        Zlib::GzipWriter.open(zip_name, Zlib::BEST_COMPRESSION) {|f| f.write(contents) }
      end
      File.utime(mtime, mtime, *files)
    end