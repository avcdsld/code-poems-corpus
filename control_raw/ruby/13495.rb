def attribute_access(ast, options = {})
      options = { type: :any, ignore_calls: false }.merge!(options)
      return [] unless ast.respond_to?(:xpath)

      unless [:any, :string, :symbol, :vivified].include?(options[:type])
        raise ArgumentError, "Node type not recognised"
      end

      case options[:type]
      when :any then
        vivified_attribute_access(ast, options) +
          standard_attribute_access(ast, options)
      when :vivified then
        vivified_attribute_access(ast, options)
      else
        standard_attribute_access(ast, options)
      end
    end