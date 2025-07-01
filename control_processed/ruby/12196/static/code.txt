def numeric_summary
      summary = "\n  median: #{median}" +
                "\n  mean: %0.4f" % mean
      if sd
        summary << "\n  std.dev.: %0.4f" % sd +
                   "\n  std.err.: %0.4f" % se
      end

      if count_values(*Daru::MISSING_VALUES).zero?
        summary << "\n  skew: %0.4f" % skew +
                   "\n  kurtosis: %0.4f" % kurtosis
      end
      summary
    end