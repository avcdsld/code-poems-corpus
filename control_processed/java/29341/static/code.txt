public void write(long singerId) {
    // [START write]
    Mutation mutation =
        Mutation.newInsertBuilder("Singer")
            .set("SingerId")
            .to(singerId)
            .set("FirstName")
            .to("Billy")
            .set("LastName")
            .to("Joel")
            .build();
    dbClient.write(Collections.singletonList(mutation));
    // [END write]
  }