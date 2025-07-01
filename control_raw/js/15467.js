function intValueExact() {
  //--int lodigit;
  var lodigit;
  //--int useexp=0;
  var useexp=0;
  //--int result;
  var result;
  //--int i=0;
  var i=0;
  //--int topdig=0;
  var topdig=0;
  // This does not use longValueExact() as the latter can be much
  // slower.
  // intcheck (from pow) relies on this to check decimal part
  if (this.ind==this.iszero)
   return 0; // easy, and quite common
  /* test and drop any trailing decimal part */
  lodigit=this.mant.length-1;
  if (this.exp<0)
   {
    lodigit=lodigit+this.exp; // reduces by -(-exp)
    /* all decimal places must be 0 */
    if ((!(this.allzero(this.mant,lodigit+1))))
     throw "intValueExact(): Decimal part non-zero: " + this.toString();
    if (lodigit<0)
     return 0; // -1<this<1
    useexp=0;
   }
  else
   {/* >=0 */
    if ((this.exp+lodigit)>9)  // early exit
     throw "intValueExact(): Conversion overflow: "+this.toString();
    useexp=this.exp;
   }
  /* convert the mantissa to binary, inline for speed */
  result=0;
  {var $16=lodigit+useexp;i=0;i:for(;i<=$16;i++){
   result=result*10;
   if (i<=lodigit)
    result=result+this.mant[i];
   }
  }/*i*/

  /* Now, if the risky length, check for overflow */
  if ((lodigit+useexp)==9)
   {
    // note we cannot just test for -ve result, as overflow can move a
    // zero into the top bit [consider 5555555555]
    topdig=div(result,1000000000); // get top digit, preserving sign
    if (topdig!=this.mant[0])
     { // digit must match and be positive
      // except in the special case ...
      if (result==-2147483648)  // looks like the special
       if (this.ind==this.isneg)  // really was negative
        if (this.mant[0]==2)
         return result; // really had top digit 2
      throw "intValueExact(): Conversion overflow: "+this.toString();
     }
   }

  /* Looks good */
  if (this.ind==this.ispos)
   return result;
  return -result;
  }