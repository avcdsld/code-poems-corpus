def date_group_items=(options)
      options.each do |date_group|
        raise ArgumentError, "date_group_items should be an array of hashes specifying the options for each date_group_item" unless date_group.is_a?(Hash)
        date_group_items << DateGroupItem.new(date_group)
      end
    end