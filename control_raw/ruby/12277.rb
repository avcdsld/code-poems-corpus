def [] *key
      return slice(*key) if key.size != 1
      key = key[0]
      case key
      when Numeric
        key
      when DateTime
        Helper.find_index_of_date(@data, key)
      when Range
        # FIXME: get_by_range is suspiciously close to just #slice,
        #   but one of specs fails when replacing it with just slice
        get_by_range(key.first, key.last)
      else
        raise ArgumentError, "Key #{key} is out of bounds" if
          Helper.key_out_of_bounds?(key, @data)

        slice(*Helper.find_date_string_bounds(key))
      end
    end