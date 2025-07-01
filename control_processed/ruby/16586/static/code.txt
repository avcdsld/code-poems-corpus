def getbinaryfile(remotefile, localfile = File.basename(remotefile),
                      blocksize = DEFAULT_BLOCKSIZE) # :yield: data
      result = nil
      if localfile
        if @resume
          rest_offset = File.size?(localfile)
          f = open(localfile, "a")
        else
          rest_offset = nil
          f = open(localfile, "w")
        end
      elsif !block_given?
        result = ""
      end
      begin
        f.binmode if localfile
        retrbinary("RETR " + remotefile.to_s, blocksize, rest_offset) do |data|
          f.write(data) if localfile
          yield(data) if block_given?
          result.concat(data) if result
        end
        return result
      ensure
        f.close if localfile
      end
    end