function(points, parameters) {
  parameters = defaultValue(parameters, defaultValue.EMPTY_OBJECT);
  /**
   * The array of points. Each point should have the format {x: X, y: Y}.
   * @type {Object[]}
   */
  this.points = defaultValue(points, []);

  /**
   * A selected point from the array above. Used internally by charting functions for hover/clicking functionality.
   * @type {Object}
   */
  this.point = undefined;

  /**
   * Unique id for this set of points.
   * @type {String}
   */
  this.id = parameters.id;

  /**
   * Name of the category for this set of points., eg. the source catalog item.
   * @type {String}
   */
  this.categoryName = parameters.categoryName;

  /**
   * Name for this set of points.
   * @type {String}
   */
  this.name = parameters.name;

  /**
   * Units of this set of points.
   * @type {String}
   */
  this.units = parameters.units;

  /**
   * CSS color code for this set of points.
   * @type {String}
   */
  this.color = parameters.color;

  /**
   * Minimum value for y axis to display, overriding minimum value in data.
   * @type {String}
   */
  this.yAxisMin = parameters.yAxisMin;

  /**
   * Maximum value for y axis to display, overriding maximum value in data.
   * @type {String}
   */
  this.yAxisMax = parameters.yAxisMax;

  /**
   * Chart type. If you want these points to be rendered with a certain way. Leave empty for auto detection.
   * @type {String}
   */
  this.type = parameters.type;

  /**
   * Click handler (called with (x, y) in data units) if some special behaviour is required on clicking.
   * @type {Function}
   */
  this.onClick = parameters.onClick;

  /**
   * Request that the chart be scaled so that this series can be shown entirely.
   * @type {Boolean}
   * @default true
   */
  this.showAll = defaultValue(parameters.showAll, true);

  this.yAxisWidth = 40;
}