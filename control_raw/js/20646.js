function processRowBuffer()
  {
    // get the row to add to the read queue
    var row = rowBuffer[rowIndex++];

    // if we just read the last row in the row buffer, clear the row buffer and
    // reset the row index so that we load the next chunk in the result stream
    // when _read() is called
    if (rowIndex === rowBuffer.length)
    {
      rowBuffer = null;
      rowIndex = 0;
    }

    // initialize the columns and column-related maps if necessary
    if (!columns)
    {
      columns = statement.getColumns();
    }
    if (!mapColumnIdToExtractFnName)
    {
      mapColumnIdToExtractFnName =
          buildMapColumnExtractFnNames(columns, fetchAsString);
    }

    // add the next row to the read queue
    process.nextTick(function()
    {
      self.push(externalizeRow(row, columns, mapColumnIdToExtractFnName));
    });
  }