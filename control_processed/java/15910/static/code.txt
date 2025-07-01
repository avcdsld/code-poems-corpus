@VisibleForTesting
  Set<DataSegment> refreshSegments(final Set<DataSegment> segments) throws IOException
  {
    final Set<DataSegment> retVal = new HashSet<>();

    // Organize segments by dataSource.
    final Map<String, TreeSet<DataSegment>> segmentMap = new TreeMap<>();

    for (DataSegment segment : segments) {
      segmentMap.computeIfAbsent(segment.getDataSource(), x -> new TreeSet<>(SEGMENT_ORDER))
                .add(segment);
    }

    for (Map.Entry<String, TreeSet<DataSegment>> entry : segmentMap.entrySet()) {
      final String dataSource = entry.getKey();
      retVal.addAll(refreshSegmentsForDataSource(dataSource, entry.getValue()));
    }

    return retVal;
  }