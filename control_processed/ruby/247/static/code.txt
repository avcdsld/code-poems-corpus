def partial_path(object, view)
        object = object.to_model if object.respond_to?(:to_model)

        path = if object.respond_to?(:to_partial_path)
          object.to_partial_path
        else
          raise ArgumentError.new("'#{object.inspect}' is not an ActiveModel-compatible object. It must implement :to_partial_path.")
        end

        if view.prefix_partial_path_with_controller_namespace
          prefixed_partial_names[path] ||= merge_prefix_into_object_path(@context_prefix, path.dup)
        else
          path
        end
      end