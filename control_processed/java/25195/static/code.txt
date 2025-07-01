public S fillWithDefaults() {
    HyperSpaceSearchCriteria defaults = null;

    if (HyperSpaceSearchCriteria.Strategy.Cartesian == strategy) {
      defaults = new HyperSpaceSearchCriteria.CartesianSearchCriteria();
    } else if (HyperSpaceSearchCriteria.Strategy.RandomDiscrete == strategy) {
      defaults = new HyperSpaceSearchCriteria.RandomDiscreteValueSearchCriteria();
    } else {
      throw new H2OIllegalArgumentException("search_criteria.strategy", strategy.toString());
    }

    fillFromImpl((I)defaults);

    return (S) this;
  }