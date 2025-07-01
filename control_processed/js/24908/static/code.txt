function pdf(x, df1, df2) {
    var p, q, f;

    if (x < 0)
      return 0;

    if (df1 <= 2) {
      if (x === 0 && df1 < 2) {
        return Infinity;
      }
      if (x === 0 && df1 === 2) {
        return 1;
      }
      return (1 / jStat.betafn(df1 / 2, df2 / 2)) *
              Math.pow(df1 / df2, df1 / 2) *
              Math.pow(x, (df1/2) - 1) *
              Math.pow((1 + (df1 / df2) * x), -(df1 + df2) / 2);
    }

    p = (df1 * x) / (df2 + x * df1);
    q = df2 / (df2 + x * df1);
    f = df1 * q / 2.0;
    return f * jStat.binomial.pdf((df1 - 2) / 2, (df1 + df2 - 2) / 2, p);
  }