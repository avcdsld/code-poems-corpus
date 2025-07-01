function max() {
  var set;
  if (max.arguments.length == 2)
   {
    set = max.arguments[1];
   }
  else if (max.arguments.length == 1)
   {
    set = this.plainMC;
   }
  else
   {
    throw "max(): " + max.arguments.length + " arguments given; expected 1 or 2";
   }
  var rhs = max.arguments[0];
  if ((this.compareTo(rhs,set))>=0)
   return this.plus(set);
  else
   return rhs.plus(set);
  }