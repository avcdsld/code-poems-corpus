def verify_default_value_matches_verify_block
      @available_options.each do |item|
        next unless item.verify_block && item.default_value

        begin
          unless @values[item.key] # this is important to not verify if there already is a value there
            item.verify_block.call(item.default_value)
          end
        rescue => ex
          UI.error(ex)
          UI.user_error!("Invalid default value for #{item.key}, doesn't match verify_block")
        end
      end
    end