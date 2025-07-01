def charlock_detect(str)
      if defined? CharlockHolmes::EncodingDetector
        if detected = CharlockHolmes::EncodingDetector.detect(str)
          str.force_encoding(detected[:encoding]) if detected[:encoding]
        end
      end

      str
    end