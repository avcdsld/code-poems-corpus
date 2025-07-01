def status
      if current_build && current_build.building?
        "building"
      elsif build = completed_builds.first
        if build.green?
          "green"
        elsif build.red?
          "red"
        end
      elsif completed_builds.empty? || builds.empty?
        "no build"
      else
        raise Error, "unexpected branch status: #{id.inspect}"
      end
    end