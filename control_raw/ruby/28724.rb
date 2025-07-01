def to_cpp(qualified = true)
      type = NodeCache.find(attributes["type"])

      post_const = container ? " const" : ""
      pre_const = container ? "" : "const "

      "#{pre_const}#{type.to_cpp(qualified)}#{post_const}"
    end