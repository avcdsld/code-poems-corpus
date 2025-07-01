def visitor(klass)
      visitor = visitor_by_module[klass]

      unless visitor
        klass.ancestors.each do |mod|
          visitor = visitor_by_module[mod]

          unless visitor
            visitor = visitor_by_module_name[mod.name]
          end

          if visitor
            visitor_by_module[klass] = visitor

            break
          end
        end
      end

      unless visitor
        raise TypeError,
              "No visitor that handles #{klass} or " \
                    "any of its ancestors (#{klass.ancestors.map(&:name).to_sentence})"
      end

      visitor
    end