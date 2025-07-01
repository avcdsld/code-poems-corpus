def raw_vector_with(word_list)
      vec = if $GSL
              GSL::Vector.alloc(word_list.size)
            else
              Array.new(word_list.size, 0)
            end

      @word_hash.each_key do |word|
        vec[word_list[word]] = @word_hash[word] if word_list[word]
      end

      # Perform the scaling transform and force floating point arithmetic
      if $GSL
        sum = 0.0
        vec.each { |v| sum += v }
        total_words = sum
      else
        total_words = vec.reduce(0, :+).to_f
      end

      total_unique_words = 0

      if $GSL
        vec.each { |word| total_unique_words += 1 if word != 0.0 }
      else
        total_unique_words = vec.count { |word| word != 0 }
      end

      # Perform first-order association transform if this vector has more
      # then one word in it.
      if total_words > 1.0 && total_unique_words > 1
        weighted_total = 0.0
        # Cache calculations, this takes too long on large indexes
        cached_calcs = Hash.new do |hash, term|
          hash[term] = ((term / total_words) * Math.log(term / total_words))
        end

        vec.each do |term|
          weighted_total += cached_calcs[term] if term > 0.0
        end

        # Cache calculations, this takes too long on large indexes
        cached_calcs = Hash.new do |hash, val|
          hash[val] = Math.log(val + 1) / -weighted_total
        end

        vec.collect! do |val|
          cached_calcs[val]
        end
      end

      if $GSL
        @raw_norm   = vec.normalize
        @raw_vector = vec
      else
        @raw_norm   = Vector[*vec].normalize
        @raw_vector = Vector[*vec]
      end
    end