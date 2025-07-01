def validate(representation)
      return {} if representation.nil? || representation.empty?

      if representation.respond_to?(:to_hash)
        representation.to_hash.dup
      else
        raise InvalidRepresentationError.new(
          "Invalid representation for resource (got #{representation.class}, expected Hash). " \
          "Is your web server returning JSON HAL data with a 'Content-Type: application/hal+json' header?",
          representation
        )
      end
    end