protected void preamble(SB sb, int subtree) throws RuntimeException {
    String subt = subtree > 0 ? "_" + String.valueOf(subtree) : "";
    sb.p("class ").p(_javaClassName).p(subt).p(" {").nl().ii(1);
    sb.ip("static final double score0").p("(double[] data) {").nl().ii(1); // predict method for one tree
    sb.ip("double pred = ");
  }