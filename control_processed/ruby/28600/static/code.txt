def mk_distribution(*args)
      flat = args.flatten
      raw = flat.first.is_a?(String) ? flat.first.split : flat

      hash = raw.each_with_object(Hash.new(0)) do |v, sum|
        sum[v] += 1
        sum
      end

      hash.to_a.map { |a, b| [b, a.to_f] }
    end