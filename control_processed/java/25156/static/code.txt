public static String withOrdinalIndicator(long i) {
    String ord;
    // Grab second to last digit
    int d = (int) (Math.abs(i) / Math.pow(10, 1)) % 10;
    if (d == 1) ord = "th"; //teen values all end in "th"
    else { // not a weird teen number
      d = (int) (Math.abs(i) / Math.pow(10, 0)) % 10;
      switch (d) {
        case 1: ord = "st"; break;
        case 2: ord = "nd"; break;
        case 3: ord = "rd"; break;
        default: ord = "th";
      }
    }
    return i+ord;
  }