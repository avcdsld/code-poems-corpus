def non_code?(line_no)
      line_cov = coverage.find { |ln, _cov| ln == line_no }
      !line_cov
    end