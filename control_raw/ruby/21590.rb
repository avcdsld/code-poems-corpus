def to_s

      s = []
      s << self.class.name
      s << "  at:      #{@fei.sid} (#{@fei.expid})"
      s << "  action:  #{@type.inspect}"
      s << "  tree:"

      s.concat(
        Ruote::Reader.to_radial(@tree).split("\n").map { |l| "    | #{l}" })

      s.join("\n")
    end