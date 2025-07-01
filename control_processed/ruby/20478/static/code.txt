def dependencies_of(names)
      names = Array === names ? names.dup : names.to_a
      assert_strings!(names)

      deps = Set.new
      until names.empty?
        name = names.shift
        next if deps.include?(name)

        deps << name
        names.concat index[name].dependencies.map(&:name)
      end
      deps.to_a
    end