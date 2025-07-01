function toFixed (value, precision, roundingFunction, optionals) {
    var power = Math.pow(10, precision),
      optionalsRegExp,
      output;

    //roundingFunction = (roundingFunction !== undefined ? roundingFunction : Math.round);
    // Multiply up by precision, round accurately, then divide and use native toFixed():
    output = (roundingFunction(value * power) / power).toFixed(precision);

    if (optionals) {
      optionalsRegExp = new RegExp('0{1,' + optionals + '}$');
      output = output.replace(optionalsRegExp, '');
    }

    return output;
  }