def dates_with_counts_from(response)
      entries = response.fetch('dates', EMPTY_HASH).map do |date, count|
        [Types::Date.deserialize(date), count.to_i]
      end
      Hash[entries]
    end