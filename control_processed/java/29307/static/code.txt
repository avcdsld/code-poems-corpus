public void runQueryPermanentTable(String destinationDataset, String destinationTable)
      throws InterruptedException {
    // [START bigquery_query_destination_table]
    // BigQuery bigquery = BigQueryOptions.getDefaultInstance().getService();
    // String destinationDataset = 'my_destination_dataset';
    // String destinationTable = 'my_destination_table';
    String query = "SELECT corpus FROM `bigquery-public-data.samples.shakespeare` GROUP BY corpus;";
    QueryJobConfiguration queryConfig =
        // Note that setUseLegacySql is set to false by default
        QueryJobConfiguration.newBuilder(query)
            // Save the results of the query to a permanent table.
            .setDestinationTable(TableId.of(destinationDataset, destinationTable))
            .build();

    // Print the results.
    for (FieldValueList row : bigquery.query(queryConfig).iterateAll()) {
      for (FieldValue val : row) {
        System.out.printf("%s,", val.toString());
      }
      System.out.printf("\n");
    }
    // [END bigquery_query_destination_table]
  }