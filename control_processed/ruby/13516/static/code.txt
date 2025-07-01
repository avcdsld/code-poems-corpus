def json_file_to_hash(filename)
      raise "File #{filename} not found" unless File.exist?(filename)

      file = File.read(filename)
      begin
        FFI_Yajl::Parser.parse(file)
      rescue FFI_Yajl::ParseError
        raise "File #{filename} does not appear to contain valid JSON"
      end
    end