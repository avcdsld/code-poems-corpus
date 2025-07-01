def format_as_option(str, io)
      if Cri::Platform.color?(io)
        yellow(str)
      else
        str
      end
    end