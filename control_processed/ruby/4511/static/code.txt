def region_prefix(leading_zero = true)
      region_prefix = rand(2..9).to_s + FFaker.numerify('#' * rand(1..3)).to_s
      region_prefix = '0' + region_prefix if leading_zero
      region_prefix
    end