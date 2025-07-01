def composition_string
      composition.sort.map do |k, v|
        v == 1 ? k.to_s : "#{k}#{v}"
      end.join('.')
    end