def construct_error_details_map_grpc(gax_error)
      return {} unless @partial_success
      error_details_map = Hash.new { |h, k| h[k] = [] }

      error_details = ensure_array(gax_error.status_details)
      raise JSON::ParserError, 'The error details are empty.' if
        error_details.empty?
      raise JSON::ParserError, 'No partial error info in error details.' unless
        error_details[0].is_a?(
          Google::Logging::V2::WriteLogEntriesPartialErrors)
      log_entry_errors = ensure_hash(error_details[0].log_entry_errors)
      log_entry_errors.each do |index, log_entry_error|
        error_key = [log_entry_error[:code], log_entry_error[:message]].freeze
        error_details_map[error_key] << index
      end
      error_details_map
    rescue JSON::ParserError => e
      @log.warn 'Failed to extract log entry errors from the error details:' \
                " #{gax_error.details.inspect}.", error: e
      {}
    end