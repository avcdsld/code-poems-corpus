def adjusted_entropy(entropy_threshhold: 0)
      revpassword = base_password.reverse
      min_entropy = [EntropyCalculator.calculate(base_password), EntropyCalculator.calculate(revpassword)].min
      QWERTY_STRINGS.each do |qwertystr|
        qpassword = mask_qwerty_strings(base_password, qwertystr)
        qrevpassword = mask_qwerty_strings(revpassword, qwertystr)
        if qpassword != base_password
          numbits = EntropyCalculator.calculate(qpassword)
          min_entropy = [min_entropy, numbits].min
          return min_entropy if min_entropy < entropy_threshhold
        end
        if qrevpassword != revpassword
          numbits = EntropyCalculator.calculate(qrevpassword)
          min_entropy = [min_entropy, numbits].min
          return min_entropy if min_entropy < entropy_threshhold
        end
      end
      min_entropy
    end