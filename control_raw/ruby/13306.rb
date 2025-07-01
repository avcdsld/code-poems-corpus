def filter_new_members(cls)
      members = cls.all_local_members.find_all do |m|
        visible?(m) && (m[:new] || new_params?(m))
      end
      members = discard_accessors(members)
      members.sort! {|a, b| a[:name] <=> b[:name] }
    end