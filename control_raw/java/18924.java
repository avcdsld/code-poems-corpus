public static double getDeviancePart(double x, double mu) {
        double ret;
        if (FastMath.abs(x - mu) < 0.1 * (x + mu)) {
            double d = x - mu;
            double v = d / (x + mu);
            double s1 = v * d;
            double s = Double.NaN;
            double ej = 2.0 * x * v;
            v = v * v;
            int j = 1;
            while (s1 != s) {
                s = s1;
                ej *= v;
                s1 = s + ej / ((j * 2) + 1);
                ++j;
            }
            ret = s1;
        } else {
            ret = x * FastMath.log(x / mu) + mu - x;
        }
        return ret;
    }