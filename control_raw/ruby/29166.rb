def parse(response)
      if response.is_a? Hash
        response.each_with_object({}) do |(key, value), new_hash|
          new_hash[camel_case_to_snake_case(key).to_sym] = parse(value)
        end
      elsif response.is_a? Array
        response.map { |item| parse item }
      else
        response
      end
    end