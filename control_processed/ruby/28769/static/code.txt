def algorithm=(alg)
      if alg.kind_of?(Array) then
        if alg.size == 1 then
          @algorithm = alg.first
        else
          @algorithm = alg
        end
      else
        @algorithm = Algorithm.algorithm_from_name(alg) unless Algorithm::EXISTING == alg
      end
      return @algorithm
    end