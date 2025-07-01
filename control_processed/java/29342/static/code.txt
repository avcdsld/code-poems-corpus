public String singleUse(long singerId) {
    // [START singleUse]
    String column = "FirstName";
    Struct row =
        dbClient.singleUse().readRow("Singers", Key.of(singerId), Collections.singleton(column));
    String firstName = row.getString(column);
    // [END singleUse]
    return firstName;
  }