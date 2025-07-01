def level(black_point = 0.0, white_point = nil, gamma = nil)
      black_point = Float(black_point)

      white_point ||= Magick::QuantumRange - black_point
      white_point = Float(white_point)

      gamma_arg = gamma
      gamma ||= 1.0
      gamma = Float(gamma)

      if gamma.abs > 10.0 || white_point.abs <= 10.0 || white_point.abs < gamma.abs
        gamma, white_point = white_point, gamma
        white_point = Magick::QuantumRange - black_point unless gamma_arg
      end

      level2(black_point, white_point, gamma)
    end