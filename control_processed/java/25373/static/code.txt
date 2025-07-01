public double recall() {
    if(!isBinary())throw new UnsupportedOperationException("recall is only implemented for 2 class problems.");
    if(tooLarge())throw new UnsupportedOperationException("recall cannot be computed: too many classes");
    double tp = _cm[1][1];
    double fn = _cm[1][0];
    return tp / (tp + fn);
  }