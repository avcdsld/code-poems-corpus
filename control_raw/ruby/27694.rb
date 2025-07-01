def to_s(base=2)
    n = Bits.power_of_two(base)
    if n
      digits = (size+n-1)/n
      #{ }"%0#{digits}d" % @v.to_s(base)
      Numerals::Format[:fix, base: base].set_leading_zeros(digits).write(@v)
    else
      @v.to_s(base)
    end
  end