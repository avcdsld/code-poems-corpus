function tableStructureFromStringData(stringData) {
    // sourceData can be either json (starts with a '[') or csv format (contains a true line feed or '\n'; \n is replaced with a real linefeed).
    if (!defined(stringData) || stringData.length < 2) {
      return;
    }
    // We prevent ALT, LON and LAT from being chosen, since we know this is a non-geo csv already.
    const result = new TableStructure("chart", {
      unallowedTypes: [VarType.ALT, VarType.LAT, VarType.LON]
    });
    if (stringData[0] === "[") {
      // Treat as json.
      const json = JSON.parse(stringData.replace(/&quot;/g, '"'));
      return TableStructure.fromJson(json, result);
    }
    if (stringData.indexOf("\\n") >= 0 || stringData.indexOf("\n") >= 0) {
      // Treat as csv.
      return TableStructure.fromCsv(stringData.replace(/\\n/g, "\n"), result);
    }
  }