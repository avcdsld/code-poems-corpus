function finish(set, strip) {
  //--int d=0;
  var d=0;
  //--int i=0;
  var i=0;
  //--byte newmant[]=null;
  var newmant=null;
  //--int mag=0;
  var mag=0;
  //--int sig=0;
  var sig=0;
  /* Round if mantissa too long and digits requested */
  if (set.digits!=0)
   if (this.mant.length>set.digits)
    this.round(set);

  /* If strip requested (and standard formatting), remove
     insignificant trailing zeros. */
  if (strip)
   if (set.form!=MathContext.prototype.PLAIN)
    {
     d=this.mant.length;
     /* see if we need to drop any trailing zeros */
     {i=d-1;i:for(;i>=1;i--){
      if (this.mant[i]!=0)
       break i;
      d--;
      this.exp++;
      }
     }/*i*/
     if (d<this.mant.length)
      {/* need to reduce */
       newmant=new Array(d);
       //--java.lang.System.arraycopy((java.lang.Object)this.mant,0,(java.lang.Object)newmant,0,d);
       this.arraycopy(this.mant,0,newmant,0,d);
       this.mant=newmant;
      }
    }

  this.form=MathContext.prototype.PLAIN; // preset

  /* Now check for leading- and all- zeros in mantissa */
  {var $26=this.mant.length;i=0;i:for(;$26>0;$26--,i++){
   if (this.mant[i]!=0)
    {
     // non-0 result; ind will be correct
     // remove leading zeros [e.g., after subtract]
     if (i>0)
      {delead:do{
       newmant=new Array(this.mant.length-i);
       //--java.lang.System.arraycopy((java.lang.Object)this.mant,i,(java.lang.Object)newmant,0,this.mant.length-i);
       this.arraycopy(this.mant,i,newmant,0,this.mant.length-i);
       this.mant=newmant;
      }while(false);}/*delead*/
     // now determine form if not PLAIN
     mag=this.exp+this.mant.length;
     if (mag>0)
      { // most common path
       if (mag>set.digits)
        if (set.digits!=0)
         this.form=set.form;
       if ((mag-1)<=this.MaxExp)
        return this; // no overflow; quick return
      }
     else
      if (mag<(-5))
       this.form=set.form;
     /* check for overflow */
     mag--;
     if ((mag<this.MinExp)||(mag>this.MaxExp))
      {overflow:do{
       // possible reprieve if form is engineering
       if (this.form==MathContext.prototype.ENGINEERING)
        {
         sig=mag%3; // leftover
         if (sig<0)
          sig=3+sig; // negative exponent
         mag=mag-sig; // exponent to use
         // 1999.06.29: second test here must be MaxExp
         if (mag>=this.MinExp)
          if (mag<=this.MaxExp)
           break overflow;
        }
       throw "finish(): Exponent Overflow: "+mag;
      }while(false);}/*overflow*/
     return this;
    }
   }
  }/*i*/

  // Drop through to here only if mantissa is all zeros
  this.ind=this.iszero;
  {/*select*/
  if (set.form!=MathContext.prototype.PLAIN)
   this.exp=0; // standard result; go to '0'
  else if (this.exp>0)
   this.exp=0; // +ve exponent also goes to '0'
  else{
   // a plain number with -ve exponent; preserve and check exponent
   if (this.exp<this.MinExp)
    throw "finish(): Exponent Overflow: "+this.exp;
  }
  }
  this.mant=this.ZERO.mant; // canonical mantissa
  return this;
  }