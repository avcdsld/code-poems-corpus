function gmlToGeoJson(xml) {
  if (typeof xml === "string") {
    var parser = new DOMParser();
    xml = parser.parseFromString(xml, "text/xml");
  }

  var result = [];

  var featureCollection = xml.documentElement;

  var featureMembers = featureCollection.getElementsByTagNameNS(
    gmlNamespace,
    "featureMember"
  );
  for (
    var featureIndex = 0;
    featureIndex < featureMembers.length;
    ++featureIndex
  ) {
    var featureMember = featureMembers[featureIndex];

    var properties = {};

    getGmlPropertiesRecursively(featureMember, properties);

    var feature = {
      type: "Feature",
      geometry: getGmlGeometry(featureMember),
      properties: properties
    };

    if (defined(feature.geometry)) {
      result.push(feature);
    }
  }

  return {
    type: "FeatureCollection",
    crs: { type: "EPSG", properties: { code: "4326" } },
    features: result
  };
}