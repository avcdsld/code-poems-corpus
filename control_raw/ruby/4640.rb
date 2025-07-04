def match(tokens, definitions)
      token_index = 0
      @pattern.each do |elements|
        was_optional = false
        elements = [elements] unless elements.is_a?(Array)

        elements.each_index do |i|
          name = elements[i].to_s
          optional = name[-1, 1] == '?'
          name = name.chop if optional

          case elements[i]
          when Symbol
            if tags_match?(name, tokens, token_index)
              token_index += 1
              break
            else
              if optional
                was_optional = true
                next
              elsif i + 1 < elements.count
                next
              else
                return false unless was_optional
              end
            end

          when String
            return true if optional && token_index == tokens.size

            if definitions.key?(name.to_sym)
              sub_handlers = definitions[name.to_sym]
            else
              raise "Invalid subset #{name} specified"
            end

            sub_handlers.each do |sub_handler|
              return true if sub_handler.match(tokens[token_index..tokens.size], definitions)
            end
          else
            raise "Invalid match type: #{elements[i].class}"
          end
        end

      end

      return false if token_index != tokens.size
      return true
    end