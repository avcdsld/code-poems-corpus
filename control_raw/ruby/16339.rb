def run_validations(validations = nil)
      # Default to running the class level validations
      validations ||= self.class.validations_to_run

      promise = Promise.new.resolve(nil)
      if validations

        # Run through each validation
        validations.each_pair do |field_name, options|
          promise = promise.then { run_validation(field_name, options) }
        end
      end

      promise
    end