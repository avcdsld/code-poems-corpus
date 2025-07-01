function isSameDay(d1, d2) {
      return d1.getDate() == d2.getDate() && isSameMonthAndYear(d1, d2);
    }