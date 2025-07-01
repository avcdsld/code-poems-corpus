def tags(instance)
      return [] if instance.groupSet.nil? || instance.groupSet.item.empty?
      instance.groupSet.item.collect{|g| g.groupId }.select {|s| s.start_with? "#poolparty"}
    end