def to_string_interpolation(node_or_interp)
      unless node_or_interp.is_a?(Interpolation)
        node = node_or_interp
        return string_literal(node.value.to_s) if node.is_a?(Literal)
        if node.is_a?(StringInterpolation)
          return concat(string_literal(node.quote), concat(node, string_literal(node.quote)))
        end
        return StringInterpolation.new(string_literal(""), node, string_literal(""))
      end

      interp = node_or_interp
      after_string_or_interp =
        if interp.after
          to_string_interpolation(interp.after)
        else
          string_literal("")
        end
      if interp.after && interp.whitespace_after
        after_string_or_interp = concat(string_literal(' '), after_string_or_interp)
      end

      mid_string_or_interp = to_string_interpolation(interp.mid)

      before_string_or_interp =
        if interp.before
          to_string_interpolation(interp.before)
        else
          string_literal("")
        end
      if interp.before && interp.whitespace_before
        before_string_or_interp = concat(before_string_or_interp, string_literal(' '))
      end

      concat(before_string_or_interp, concat(mid_string_or_interp, after_string_or_interp))
    end