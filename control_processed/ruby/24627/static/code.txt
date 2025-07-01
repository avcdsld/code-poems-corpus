def gcd_decomposition(a,b)
      if b == 0
        [a, 1, 0]
      else
        n = a/b
        c = a % b
        r = gcd_decomposition(b,c)
        [r[0], r[2], r[1]-r[2]*n]
      end
    end