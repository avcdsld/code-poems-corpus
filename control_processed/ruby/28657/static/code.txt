def next_item
      return nil unless more_items?
      return response.cursor if response.respond_to?(:cursor)
      response.offset + response.limit
    rescue StandardError
      nil
    end