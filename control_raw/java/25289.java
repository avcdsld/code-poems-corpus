public double gammaDenom(double w, double y, double z, double f) {
    switch (distribution) {
      case gaussian:
      case gamma:
        return w;
      case bernoulli:
      case quasibinomial:
        double ff = y-z;
        return w * ff*(1-ff);
      case multinomial:
        double absz = Math.abs(z);
        return w * (absz*(1-absz));
      case poisson:
        return w * (y-z); //y-z == exp(f)
      case tweedie:
        return w * exp(f*(2- tweediePower));
      case modified_huber:
        double yf = (2*y-1)*f;
        if (yf < -1) return -w*4*yf;
        else if (yf > 1) return 0;
        else return w*(1-yf)*(1-yf);
      default:
        throw H2O.unimpl();
    }
  }