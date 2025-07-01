def move(x, y)
      (x < 0 ? backward(-x) : (x > 0 ? forward(x) : '')) +
      (y < 0 ? down(-y) : (y > 0 ? up(y) : ''))
    end