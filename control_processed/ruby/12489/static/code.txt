def decoded_gzip_body
      unless gzip = Zlib::GzipReader.new(StringIO.new(raw_body))
        raise ArgumentError, "Unable to create Zlib::GzipReader"
      end
      gzip.read
    ensure
      gzip.close if gzip
    end