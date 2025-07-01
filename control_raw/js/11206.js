function formatBanner(message, options) {
  options = options || {};

  var width = options.width === undefined ? 80 : options.width;
  var marginLeft = options.marginLeft === undefined ? 0 : options.marginLeft;
  var marginRight = options.marginRight === undefined ? 0 : options.marginRight;
  var paddingTop = options.paddingTop === undefined ? 0 : options.paddingTop;
  var paddingBottom = options.paddingBottom === undefined ? 0 : options.paddingBottom;
  var paddingLeft = options.paddingLeft === undefined ? 2 : options.paddingLeft;
  var paddingRight = options.paddingRight === undefined ? 2 : options.paddingRight;

  var horizSpacing = marginLeft + paddingLeft + paddingRight + marginRight;
  // 2 for the banner borders
  var maxLineWidth = width - horizSpacing - 2;
  var wrap = wordwrap(maxLineWidth);
  var body = wrap(message);

  var left = spaces(marginLeft) + VERTICAL_LINE + spaces(paddingLeft);
  var right = spaces(paddingRight) + VERTICAL_LINE + spaces(marginRight);
  var bodyLines = [].concat(
    arrayOf('', paddingTop),
    body.split('\n'),
    arrayOf('', paddingBottom)
  ).map(function(line) {
    var padding = spaces(Math.max(0, maxLineWidth - line.length));
    return left + (options.chalkFunction ? options.chalkFunction(line) : line) + padding + right;
  });

  var horizontalBorderLine = repeatString(
    HORIZONTAL_LINE,
    width - marginLeft - marginRight - 2
  );
  var top =
    spaces(marginLeft) +
    TOP_LEFT +
    horizontalBorderLine +
    TOP_RIGHT +
    spaces(marginRight);
  var bottom =
    spaces(marginLeft) +
    BOTTOM_LEFT +
    horizontalBorderLine +
    BOTTOM_RIGHT +
    spaces(marginRight);
  return [].concat(top, bodyLines, bottom).join('\n');
}