public String toFString(int digits) {
        if (b.compareTo(BigInteger.ONE) != 0) {
            MathContext mc = new MathContext(digits, RoundingMode.DOWN);
            BigDecimal f = (new BigDecimal(a)).divide(new BigDecimal(b), mc);
            return (f.toString());
        } else {
            return a.toString();
        }
    }