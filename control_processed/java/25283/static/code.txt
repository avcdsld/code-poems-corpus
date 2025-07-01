public static double exp(double x) {
    double val = Math.min(MAX, Math.exp(x));
//    if (val == MAX) Log.warn("Exp overflow: exp(" + x + ") truncated to " + MAX);
    return val;
  }