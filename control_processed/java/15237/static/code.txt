public Collection<DataSegment> getLazyAllSegments()
  {
    return CollectionUtils.createLazyCollectionFromStream(
        () -> dataSources.values().stream().flatMap(dataSource -> dataSource.getSegments().stream()),
        totalSegments
    );
  }