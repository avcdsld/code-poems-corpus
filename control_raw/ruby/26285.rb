def sample_range(range, seed=nil)
      srand seed if seed
      rand * (range.end - range.begin) + range.begin
    end