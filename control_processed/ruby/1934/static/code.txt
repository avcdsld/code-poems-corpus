def string_to_hash(markup)
      options = {}

      if match = markup.match(Syntax)
        markup.scan(TagAttributes) do |key, value|
          options[key.to_sym] = value.gsub(/\A"|"\z/, "")
        end
      end

      options
    end