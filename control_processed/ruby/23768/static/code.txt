def unique_id
      # check all_data instead of data, as we have to not reuse deleted key
      ids = Set.new(all_data.map { |e| e[:key] })
      id = 1
      loop do
        return id.to_s unless ids.include?(id.to_s)

        id += 1
      end
    end