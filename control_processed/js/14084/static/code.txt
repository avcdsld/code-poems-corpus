function(terria) {
  CatalogItem.call(this, terria);

  this._dataUrl = undefined;
  this._dataUrlType = undefined;
  this._metadataUrl = undefined;
  this._geoJsonItem = undefined;

  /**
   * Gets or sets the WFS feature type names.
   * @type {String}
   */
  this.typeNames = "";

  /**
   * Gets or sets a value indicating whether we should request GeoJSON from the WFS server.  If this property
   * and {@link WebFeatureServiceCatalogItem#requestGeoJson} are both true, we'll request GeoJSON first and
   * only fall back on trying GML if the GeoJSON request fails.
   * @type {Boolean}
   * @default true
   */
  this.requestGeoJson = true;

  /**
   * Gets or sets a value indicating whether we should request GML from the WFS server.  If this property
   * and {@link WebFeatureServiceCatalogItem#requestGeoJson} are both true, we'll request GeoJSON first and
   * only fall back on trying GML if the GeoJSON request fails.
   * @type {Boolean}
   * @default true
   */
  this.requestGml = true;

  /**
   * Gets or sets the additional parameters to pass to the WFS server when requesting geometry.
   * All parameter names must be entered in lowercase in order to be consistent with references in TerrisJS code.
   * @type {Object}
   */
  this.parameters = {};

  knockout.track(this, [
    "_dataUrl",
    "_dataUrlType",
    "_metadataUrl",
    "typeNames",
    "requestGeoJson",
    "requestGml"
  ]);

  // dataUrl, metadataUrl, and legendUrl are derived from url if not explicitly specified.
  overrideProperty(this, "dataUrl", {
    get: function() {
      var url = this._dataUrl;
      if (!defined(url)) {
        url = this.url;
      }

      if (this.dataUrlType === "wfs") {
        url = new URI(cleanUrl(url))
          .setQuery(
            combine(
              {
                service: "WFS",
                version: "1.1.0",
                request: "GetFeature",
                typeName: this.typeNames,
                srsName: "EPSG:4326",
                maxFeatures: "1000"
              },
              this.parameters
            )
          )
          .toString();
      }

      return url;
    },
    set: function(value) {
      this._dataUrl = value;
    }
  });

  overrideProperty(this, "dataUrlType", {
    get: function() {
      if (defined(this._dataUrlType)) {
        return this._dataUrlType;
      } else {
        return "wfs";
      }
    },
    set: function(value) {
      this._dataUrlType = value;
    }
  });

  overrideProperty(this, "metadataUrl", {
    get: function() {
      if (defined(this._metadataUrl)) {
        return this._metadataUrl;
      }

      return new URI(cleanUrl(this.url))
        .setQuery(
          combine(
            {
              service: "WFS",
              version: "1.1.0",
              request: "GetCapabilities"
            },
            this.parameters
          )
        )
        .toString();
    },
    set: function(value) {
      this._metadataUrl = value;
    }
  });
}