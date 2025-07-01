function _createNewCell(rowData, rowIndex, colIndex, prevCell) {
  const cellData = rowData[colIndex];
  let newCell;

  if (util.isExisty(cellData.colMergeWith)) {
    const {colMergeWith} = cellData;
    const merger = rowData[colMergeWith];
    const lastMergedCellIndex = colMergeWith + merger.colspan - 1;

    if (util.isExisty(merger.rowMergeWith) && prevCell) {
      newCell = util.extend({}, prevCell);
    } else if (lastMergedCellIndex > colIndex) {
      merger.colspan += 1;
      newCell = util.extend({}, cellData);
    }
  } else if (cellData.colspan > 1) {
    cellData.colspan += 1;
    newCell = _createColMergedCell(colIndex, cellData.nodeName);
  }

  if (!newCell) {
    newCell = dataHandler.createBasicCell(rowIndex, colIndex + 1, cellData.nodeName);
  }

  return newCell;
}