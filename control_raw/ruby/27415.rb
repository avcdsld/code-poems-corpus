def encode_dump(dump)
      dump = dump.read unless dump.is_a?(String)

      enc = CharlockHolmes::EncodingDetector.detect(dump)
      if enc[:encoding] != 'UTF-8'
        puts "Converting `#{enc[:encoding]}` to `UTF-8`".yellow
        dump = CharlockHolmes::Converter.convert dump, enc[:encoding], 'UTF-8'
      end
      dump
    end