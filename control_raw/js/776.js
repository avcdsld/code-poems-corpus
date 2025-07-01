function(
    firstPattern, secondPattern, dateTimeSymbols, useFirstDateOnFirstPattern) {
  /**
   * Formatter_ to format the first part of the date interval.
   * @private {!DateTimeFormat}
   */
  this.firstPartFormatter_ = new DateTimeFormat(firstPattern, dateTimeSymbols);

  /**
   * Formatter_ to format the second part of the date interval.
   * @private {!DateTimeFormat}
   */
  this.secondPartFormatter_ =
      new DateTimeFormat(secondPattern, dateTimeSymbols);

  /**
   * Specifies if the first or the second date should be formatted by the
   * formatter of the first or second part of the date interval.
   * @private {boolean}
   */
  this.useFirstDateOnFirstPattern_ = useFirstDateOnFirstPattern;
}