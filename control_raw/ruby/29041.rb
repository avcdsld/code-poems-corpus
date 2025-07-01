def wakati str
      mincost_path=parse(str).mincost_path
      return nil if mincost_path.nil?
      return mincost_path.map{|node|node.word.surface}
    end