function subtract() {
  var set;
  if (subtract.arguments.length == 2)
   {
    set = subtract.arguments[1];
   }
  else if (subtract.arguments.length == 1)
   {
    set = this.plainMC;
   }
  else
   {
    throw "subtract(): " + subtract.arguments.length + " arguments given; expected 1 or 2";
   }
  var rhs = subtract.arguments[0];
  //--com.ibm.icu.math.BigDecimal newrhs;
  var newrhs;
  if (set.lostDigits)
   this.checkdigits(rhs,set.digits);
  // [add will recheck .. but would report -rhs]
  /* carry out the subtraction */
  // we could fastpath -0, but it is too rare.
  newrhs=this.clone(rhs); // safe copy
  newrhs.ind=-newrhs.ind; // prepare to subtract
  return this.add(newrhs,set); // arithmetic
  }