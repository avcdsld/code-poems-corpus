def process_response_errors
        if self.response_errors && self.response_errors.any?
          self.response_errors.each do |error|
            key = error[:attribute] && !error[:attribute].empty? ? error[:attribute] : :base
            val = error[:value] && !error[:value].empty? ? error[:value] : error[:title]
            self.errors[key.to_sym] << val
          end
        end
      end