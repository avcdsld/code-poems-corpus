function loadTableFromCsv(item, csvString) {
  var tableStyle = item._tableStyle;
  var options = {
    idColumnNames: item.idColumns,
    isSampled: item.isSampled,
    initialTimeSource: item.initialTimeSource,
    displayDuration: tableStyle.displayDuration,
    replaceWithNullValues: tableStyle.replaceWithNullValues,
    replaceWithZeroValues: tableStyle.replaceWithZeroValues,
    columnOptions: tableStyle.columns // may contain per-column replacements for these
  };
  var tableStructure = new TableStructure(undefined, options);
  tableStructure.loadFromCsv(csvString);
  return item.initializeFromTableStructure(tableStructure);
}