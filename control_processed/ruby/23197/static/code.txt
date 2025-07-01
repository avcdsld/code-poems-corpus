def anonymous_name(id)
      name = "#{id}_#{Socket.gethostname}_#{Process.pid}_#{rand(1000000)}"
      name = name.gsub('.', '_')
      name = name.gsub('-', '_')
      name.gsub(':', '_')
    end