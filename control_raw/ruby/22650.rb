def logout
      unless @log_file_path.nil?
        if Hpe3parSdk.logger != nil
          Hpe3parSdk.logger.close
          Hpe3parSdk.logger = nil
        end
      end
      begin
        @http.unauthenticate
      rescue Hpe3parSdk::HPE3PARException => ex
        #Do nothing
      end
    end