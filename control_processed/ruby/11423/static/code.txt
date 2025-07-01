def update_statistics(category, number)
      return number.map { |n| update_statistics(category, n) } if number.is_a?(Array)

      @categories[category] ||= { hits: 0, sum: 0, mean: 0.0, sum_of_squares: 0.0, min: number, max: number,
                                  buckets: Array.new(@number_of_buckets, 0) }

      delta = number - @categories[category][:mean]

      @categories[category][:hits]           += 1
      @categories[category][:mean]           += (delta / @categories[category][:hits])
      @categories[category][:sum_of_squares] += delta * (number - @categories[category][:mean])
      @categories[category][:sum]            += number
      @categories[category][:min]             = number if number < @categories[category][:min]
      @categories[category][:max]             = number if number > @categories[category][:max]

      bucketize(category, number)
    end