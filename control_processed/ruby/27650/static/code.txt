def pack(force=nil)
      if File.exists? @zipfile
        if force
          File.delete @zipfile
        else
          raise "File #{@zipfile} already exists."
        end
      end

      dirname = File.dirname(@zipfile)
      raise "Dir #{dirname} is not exists." unless File.exists? dirname
      raise "Dir #{dirname} is not writable." unless File.writable? dirname

      Zip::ZipFile.open(@zipfile, Zip::ZipFile::CREATE) do |zf|
        # manifest file
        zf.get_output_stream(MANIFEST_FILE) {|o| o << Yajl::Encoder.encode(@manifest)}

        @files.each do |f, path|
          zf.add("#{CONTENT_FOLDER}/#{f}", path)
        end
      end

      begin
        File.chmod(@filemode, @zipfile)
      rescue => e
        raise "Fail to change the mode of #{@zipfile} to #{@filemode.to_s(8)}: #{e}"
      end
    end