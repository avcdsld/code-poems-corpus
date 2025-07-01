def delete(attribute, type = nil, **options)
      attribute, type, options = normalize_arguments(attribute, type, options)
      matches = where(attribute, type, options)
      matches.each do |error|
        @errors.delete(error)
      end
      matches.map(&:message)
    end