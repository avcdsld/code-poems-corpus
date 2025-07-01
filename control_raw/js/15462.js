function pow() {
  var set;
  if (pow.arguments.length == 2)
   {
    set = pow.arguments[1];
   }
  else if (pow.arguments.length == 1)
   {
    set = this.plainMC;
   }
  else
   {
    throw "pow(): " + pow.arguments.length + " arguments given; expected 1 or 2";
   }
  var rhs = pow.arguments[0];
  //--int n;
  var n;
  //--com.ibm.icu.math.BigDecimal lhs;
  var lhs;
  //--int reqdig;
  var reqdig;
  //-- int workdigits=0;
  var workdigits=0;
  //--int L=0;
  var L=0;
  //--com.ibm.icu.math.MathContext workset;
  var workset;
  //--com.ibm.icu.math.BigDecimal res;
  var res;
  //--boolean seenbit;
  var seenbit;
  //--int i=0;
  var i=0;
  if (set.lostDigits)
   this.checkdigits(rhs,set.digits);
  n=rhs.intcheck(this.MinArg,this.MaxArg); // check RHS by the rules
  lhs=this; // clarified name

  reqdig=set.digits; // local copy (heavily used)
  if (reqdig==0)
   {
    if (rhs.ind==this.isneg)
     //--throw new java.lang.ArithmeticException("Negative power:"+" "+rhs.toString());
     throw "pow(): Negative power: " + rhs.toString();
    workdigits=0;
   }
  else
   {/* non-0 digits */
    if ((rhs.mant.length+rhs.exp)>reqdig)
     //--throw new java.lang.ArithmeticException("Too many digits:"+" "+rhs.toString());
     throw "pow(): Too many digits: " + rhs.toString();

    /* Round the lhs to DIGITS if need be */
    if (lhs.mant.length>reqdig)
     lhs=this.clone(lhs).round(set);

    /* L for precision calculation [see ANSI X3.274-1996] */
    L=rhs.mant.length+rhs.exp; // length without decimal zeros/exp
    workdigits=(reqdig+L)+1; // calculate the working DIGITS
   }

  /* Create a copy of set for working settings */
  // Note: no need to check for lostDigits again.
  // 1999.07.17 Note: this construction must follow RHS check
  workset=new MathContext(workdigits,set.form,false,set.roundingMode);

  res=this.ONE; // accumulator
  if (n==0)
   return res; // x**0 == 1
  if (n<0)
   n=-n; // [rhs.ind records the sign]
  seenbit=false; // set once we've seen a 1-bit
  {i=1;i:for(;;i++){ // for each bit [top bit ignored]
   //n=n+n; // shift left 1 bit
   n<<=1;
   if (n<0)
    { // top bit is set
     seenbit=true; // OK, we're off
     res=res.multiply(lhs,workset); // acc=acc*x
    }
   if (i==31)
    break i; // that was the last bit
   if ((!seenbit))
    continue i; // we don't have to square 1
   res=res.multiply(res,workset); // acc=acc*acc [square]
   }
  }/*i*/ // 32 bits
  if (rhs.ind<0)  // was a **-n [hence digits>0]
   res=this.ONE.divide(res,workset); // .. so acc=1/acc
  return res.finish(set,true); // round and strip [original digits]
  }