static Finding createFindingWithSourceProperties(SourceName sourceName) {
    try (SecurityCenterClient client = SecurityCenterClient.create()) {
      // SourceName sourceName = SourceName.of(/*organization=*/"123234324",/*source=*/
      // "423432321");

      // Use the current time as the finding "event time".
      Instant eventTime = Instant.now();

      // Controlled by caller.
      String findingId = "samplefindingid2";

      // The resource this finding applies to.  The CSCC UI can link
      // the findings for a resource to the corresponding Asset of a resource
      // if there are matches.
      String resourceName = "//cloudresourcemanager.googleapis.com/organizations/11232";

      // Define source properties values as protobuf "Value" objects.
      Value stringValue = Value.newBuilder().setStringValue("stringExample").build();
      Value numValue = Value.newBuilder().setNumberValue(1234).build();
      ImmutableMap<String, Value> sourceProperties =
          ImmutableMap.of("stringKey", stringValue, "numKey", numValue);

      // Start setting up a request to create a finding in a source.
      Finding finding =
          Finding.newBuilder()
              .setParent(sourceName.toString())
              .setState(State.ACTIVE)
              .setResourceName(resourceName)
              .setEventTime(
                  Timestamp.newBuilder()
                      .setSeconds(eventTime.getEpochSecond())
                      .setNanos(eventTime.getNano()))
              .putAllSourceProperties(sourceProperties)
              .build();

      // Call the API.
      Finding response = client.createFinding(sourceName, findingId, finding);

      System.out.println("Created Finding with Source Properties: " + response);
      return response;
    } catch (IOException e) {
      throw new RuntimeException("Couldn't create client.", e);
    }
  }