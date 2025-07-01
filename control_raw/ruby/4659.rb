def infer_media(filepath)
      require 'mime/types'
      types = MIME::Types.type_for(filepath)
      types.empty? ? 'application/octet-stream' : types.first
    rescue LoadError
      raise Github::Error::UnknownMedia.new(filepath)
    end