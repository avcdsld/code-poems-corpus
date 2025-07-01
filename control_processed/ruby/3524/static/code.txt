def to_model
      pcs = @preconditions.collect(&:to_model)
      mr = @reference ? @reference.to_model : nil
      cc = @conjunction
      HQMF::Precondition.new(@id, pcs, mr, cc, @negation)
    end