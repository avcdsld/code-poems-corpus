def add_collimator(coll)
      raise ArgumentError, "Invalid argument 'coll'. Expected CollimatorSetup, got #{coll.class}." unless coll.is_a?(CollimatorSetup)
      @collimators << coll unless @associated_collimators[coll.type]
      @associated_collimators[coll.type] = coll
    end