function loadRegionsFromWfs(regionProvider, propName) {
  if (regionProvider.serverType !== "WMS") {
    throw new DeveloperError(
      "Cannot fetch region ids for region providers that are not WMS"
    );
  }

  var baseuri = URI(regionProvider.server).addQuery({
    service: "wfs",
    version: "2.0",
    request: "getPropertyValue",
    typenames: regionProvider.layerName
  });

  // get the list of IDs that we will attempt to match against for this column
  var url = regionProvider.corsProxy.getURLProxyIfNecessary(
    baseuri.setQuery("valueReference", propName).toString()
  );

  return loadText(url).then(function(xml) {
    var obj = xml2json(xml);

    if (!defined(obj.member)) {
      console.log(xml);
      var exception = defined(obj.Exception)
        ? "<br/><br/>" + obj.Exception.ExceptionText
        : "";
      throw new TerriaError({
        title: "CSV region mapping",
        message:
          "Couldn't load region boundaries for region " + propName + exception
      });
    }

    if (!(obj.member instanceof Array)) {
      obj.member = [obj.member];
    }
    if (obj.member.length === 1 && !defined(obj.member[0])) {
      throw new TerriaError({
        title: "CSV region mapping",
        message: "Zero region boundaries found for region " + propName
      });
    }
    return {
      values: obj.member.map(function(m) {
        return m[propName];
      })
    };
  });
}