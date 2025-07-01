def next_clear_bit()
      @words.each_with_index do |word, i|
        if word == WORD_MASK
          next
        end
        return i * BITS_PER_WORD + BitSet.number_of_trailing_ones(word)
      end
      -1
    end