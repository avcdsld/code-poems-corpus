def sorting=(val)
      val = [val] if val.is_a? Hash
      sorting.set(*val)
    end