function(name, values, options) {
  this.options = defaultValue(options, defaultValue.EMPTY_OBJECT);
  // Note - if you add more options, be sure to include them in getFullOptions() too.
  VariableConcept.call(this, name, {
    parent: this.options.tableStructure,
    active: this.options.active,
    color: this.options.chartLineColor
  });
  this.id = defaultValue(this.options.id, this.id); // if options.id is provided, use it to override the default (this.id = this.name).
  this.format = this.options.format;
  this.units = this.options.units;

  this._rawValues = values;
  this._unallowedTypes = defaultValue(this.options.unallowedTypes, []);
  this._replaceWithZeroValues = defaultValue(
    this.options.replaceWithZeroValues,
    defaultReplaceWithZeroValues
  );
  this._replaceWithNullValues = defaultValue(
    this.options.replaceWithNullValues,
    defaultReplaceWithNullValues
  );
  this._type = this.options.type;
  this._subtype = this.options.subtype;
  this._isEndDate = this.options.isEndDate;
  if (!defined(this._type)) {
    this.setTypeAndSubTypeFromName();
  }

  var isNumerical = function(value) {
    return typeof value === "number";
  };

  if (this._type === VarType.SCALAR && values.some(isNumerical)) {
    // Before setting this._values, replace '-' and 'NA' etc with zero/null. Min/max values ignore nulls.
    this._values = replaceValues(
      values,
      this._replaceWithZeroValues,
      this._replaceWithNullValues
    );
  } else {
    this._values = values;
  }
  this._numericalValues = this._values && this._values.filter(isNumerical);

  var nonNullValues = this._values.filter(function(value) {
    return value !== null;
  });
  this._minimumValue = Math.min.apply(null, nonNullValues); // Note: a single NaN value makes this NaN (hence replaceValues above).
  this._maximumValue = Math.max.apply(null, nonNullValues);

  this.yAxisMin = this.options.yAxisMin;
  this.yAxisMax = this.options.yAxisMax;

  this._uniqueValues = undefined;
  this._indicesIntoUniqueValues = undefined;

  this.displayDuration = this.options.displayDuration; // undefined is fine.

  /**
   * this.dates is a version of values that has been converted to javascript Dates.
   * Only if type === VarType.TIME.
   */
  this.dates = undefined;
  /**
   * this.julianDates is a version of values that has been converted to JulianDates.
   * Only if type === VarType.TIME.
   */
  this.julianDates = undefined;
  /**
   * this.finishJulianDates is an Array of JulianDates listing the next different date in the values array, less 1 second.
   * This is populated by TableStructure, since it may depend on other columns.
   * Only if type === VarType.TIME.
   */
  this.finishJulianDates = undefined;
  /**
   * A TimeInterval Array giving when each row applies.
   * This is populated by TableStructure, since it may depend on other columns.
   * Only if type === VarType.TIME.
   */
  this._timeIntervals = undefined;
  /**
   * A DataSourceClock whose start and stop times correspond to the first and last visible row.
   * This is populated by TableStructure, since it may depend on other columns.
   * Only if type === VarType.TIME.
   */
  this._clock = undefined;

  if (defined(values) && this._type === VarType.TIME) {
    var jsDatesAndJulianDates = convertToDates(this);
    this.dates = jsDatesAndJulianDates.jsDates;
    this.julianDates = jsDatesAndJulianDates.julianDates;
    if (this.dates.length === 0) {
      // We couldn't interpret this as dates after all. Change type to scalar.
      this._type = VarType.SCALAR;
    } else {
      this._subtype = jsDatesAndJulianDates.subtype;
    }
  }

  // If it looked like a SCALAR but there are no numerical values, change type to ENUM.
  if (isNaN(this._minimumValue) && this._type === VarType.SCALAR) {
    this._type = VarType.ENUM;
  }

  // Finally, distinguish between ENUM and html tags.
  if (this._type === VarType.ENUM && looksLikeHtmlTags(this.values)) {
    this._type = VarType.TAG;
  }

  updateForType(this);

  this._formattedValues = getFormattedValues(this);

  // Track _type so that TableStructure can change columnsByType if type changes.
  // Track _values so that charts can update live with new data.
  // Track units so that we can set the units after data has loaded, and the chart panel updates.
  knockout.track(this, ["_type", "_values", "units", "_timeIntervals"]);
}