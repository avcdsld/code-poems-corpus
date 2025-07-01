function convertRawTimestampTz(rawColumnValue, column, context)
{
  var valFracSecsBig;
  var valFracSecsWithTzBig;
  var timezoneBig;
  var timezone;
  var timestampAndTZIndex;

  // compute the scale factor
  var columnScale = column.getScale();
  var scaleFactor = Math.pow(10, columnScale);

  var resultVersion = context.resultVersion;
  if (resultVersion === '0' || resultVersion === undefined)
  {
    // the values might be big so use BigNumber to do arithmetic
    valFracSecsBig =
        new BigNumber(rawColumnValue).times(scaleFactor);

    // for _tz, the timezone is baked into the value
    valFracSecsWithTzBig = valFracSecsBig;

    // extract everything but the lowest 14 bits to get the fractional seconds
    valFracSecsBig =
        valFracSecsWithTzBig.dividedBy(16384).floor();

    // extract the lowest 14 bits to get the timezone
    if (valFracSecsWithTzBig.greaterThanOrEqualTo(0))
    {
      timezoneBig = valFracSecsWithTzBig.modulo(16384);
    }
    else
    {
      timezoneBig =
          valFracSecsWithTzBig.modulo(16384).plus(16384);
    }
  }
  else
  {
    // split the value into number of seconds and timezone index
    timestampAndTZIndex = rawColumnValue.split(' ');

    // the values might be big so use BigNumber to do arithmetic
    valFracSecsBig =
        new BigNumber(timestampAndTZIndex[0]).times(scaleFactor);

    timezoneBig = new BigNumber(timestampAndTZIndex[1]);
  }

  timezone = timezoneBig.toNumber();

  // assert that timezone is valid
  Errors.assertInternal(timezone >= 0 && timezone <= 2880);

  // subtract 24 hours from the timezone to map [0, 48] to
  // [-24, 24], and convert the result to a number
  timezone = timezone - 1440;

  // create a new snowflake date
  return convertRawTimestampHelper(
      valFracSecsBig,
      columnScale,
      timezone,
      context.format).toSfDate();
}