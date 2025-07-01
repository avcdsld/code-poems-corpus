def create_versions_hash
      hash = Hash.new { |h, k| h[k] = [] }

      versions.each do |version|
        hash[version[0]] << version
      end

      hash
    end