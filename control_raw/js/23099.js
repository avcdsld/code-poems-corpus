function BatchResult(tableService, table, operations) {
  this.tableService = tableService;
  this.table = table;
  this.operations = operations;
  this.batchBoundary = 'batch_' + BatchResult._getBoundary();
  this.changesetBoundary = 'changeset_' + BatchResult._getBoundary();
}