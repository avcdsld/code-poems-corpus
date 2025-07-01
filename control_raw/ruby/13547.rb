def compare_versions(version_a, version_b)
      if version_a == version_b
        return 0
      else
        version_a_d = deconstruct_version_string(version_a)
        version_b_d = deconstruct_version_string(version_b)

        if version_a_d[0] > version_b_d[0] ||
          (version_a_d[0] == version_b_d[0] && version_a_d[1] > version_b_d[1]) ||
          (version_a_d[0] == version_b_d[0] && version_a_d[1] == version_b_d[1] && version_a_d[2] > version_b_d[2])
          return 1
        else
          return -1
        end
      end
    end