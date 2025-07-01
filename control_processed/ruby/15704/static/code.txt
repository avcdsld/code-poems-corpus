def map_specifiers_to_versions
      specifiers = {}
      processed = {}

      l = lambda do |t|
        return if processed[t.object_id]
        processed[t.object_id] = true
        t.dependencies.each do |package, spec|
          specifiers[package] ||= {}
          specifiers[package][spec.clause] ||= []
          specifiers[package][spec.clause] << spec
          spec.versions.each_value {|v| l[v]}
        end
      end

      l[@tree]
      specifiers
    end