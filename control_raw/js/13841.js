function(options) {
  this._uriTemplate = new URITemplate(options.url);

  if (typeof options.layerName !== "string") {
    throw new DeveloperError(
      "MapboxVectorTileImageryProvider requires a layer name passed as options.layerName"
    );
  }
  this._layerName = options.layerName;

  this._subdomains = defaultValue(options.subdomains, []);

  if (!(options.styleFunc instanceof Function)) {
    throw new DeveloperError(
      "MapboxVectorTileImageryProvider requires a styling function passed as options.styleFunc"
    );
  }
  this._styleFunc = options.styleFunc;

  this._tilingScheme = new WebMercatorTilingScheme();

  this._tileWidth = 256;
  this._tileHeight = 256;

  this._minimumLevel = defaultValue(options.minimumZoom, 0);
  this._maximumLevel = defaultValue(options.maximumZoom, Infinity);
  this._maximumNativeLevel = defaultValue(
    options.maximumNativeZoom,
    this._maximumLevel
  );

  this._rectangle = defined(options.rectangle)
    ? Rectangle.intersection(options.rectangle, this._tilingScheme.rectangle)
    : this._tilingScheme.rectangle;
  this._uniqueIdProp = options.uniqueIdProp;
  this._featureInfoFunc = options.featureInfoFunc;
  //this._featurePicking = options.featurePicking;

  // Check the number of tiles at the minimum level.  If it's more than four,
  // throw an exception, because starting at the higher minimum
  // level will cause too many tiles to be downloaded and rendered.
  var swTile = this._tilingScheme.positionToTileXY(
    Rectangle.southwest(this._rectangle),
    this._minimumLevel
  );
  var neTile = this._tilingScheme.positionToTileXY(
    Rectangle.northeast(this._rectangle),
    this._minimumLevel
  );
  var tileCount =
    (Math.abs(neTile.x - swTile.x) + 1) * (Math.abs(neTile.y - swTile.y) + 1);
  if (tileCount > 4) {
    throw new DeveloperError(
      "The imagery provider's rectangle and minimumLevel indicate that there are " +
        tileCount +
        " tiles at the minimum level. Imagery providers with more than four tiles at the minimum level are not supported."
    );
  }

  this._errorEvent = new CesiumEvent();

  this._ready = true;
}