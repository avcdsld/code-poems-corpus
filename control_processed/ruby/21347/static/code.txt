def has_error?(error_message, options = {})
      error_found = false
      if options[:field]
        first('.field.has-error', minimum: 1) # wait for any errors to come from validation
        all(".field.has-error").each do |field_container|
          if !error_found
            within(field_container) do
              if has_field?(options[:field], wait: false) && has_css?(".error", text: error_message, wait: false)
                error_found = true
              end
            end
          end
        end
      else
        if first(".form-error-box .error", text: error_message)
          error_found = true
        end
      end

      unless error_found
        failure_text = "Unable to find error message #{error_message.inspect}"
        if options[:field]
          failure_text += " on field #{options[:field].inspect}"
        end
        raise Capybara::ElementNotFound.new failure_text
      end

      true
    end