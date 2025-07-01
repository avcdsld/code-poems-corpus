def insert_orphans(cls)
      members = @orphans.find_all {|node| node[:owner] == cls[:name] }
      members.each do |node|
        add_to_class(cls, node)
        @orphans.delete(node)
      end
    end