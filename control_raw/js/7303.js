function Metric(key, value, ts) {
  var m = this;
  this.key = key;
  this.value = value;
  this.ts = ts;

  // return a string representation of this metric appropriate 
  // for sending to the graphite collector. does not include
  // a trailing newline.
  this.toText = function() {
    return m.key + " " + m.value + " " + m.ts;
  };

  this.toPickle = function() {
    return MARK + STRING + '\'' + m.key + '\'\n' + MARK + LONG + m.ts + 'L\n' + STRING + '\'' + m.value + '\'\n' + TUPLE + TUPLE + APPEND;
  };
}