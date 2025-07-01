def chunk_distance(my_chunk, their_chunk)
      my_chunk = "0" if my_chunk.nil?
      their_chunk = "0" if their_chunk.nil?

      if i?(my_chunk) && i?(their_chunk)
        return [(my_chunk.to_i - their_chunk.to_i).abs, 99].min
      else
        return [Text::Levenshtein.distance(my_chunk.upcase, their_chunk.upcase), 99].min
      end
    end