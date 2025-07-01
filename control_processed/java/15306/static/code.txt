public static TreeSet<DataSegment> createAvailableSegmentsSet(Iterable<DataSegment> availableSegments)
  {
    TreeSet<DataSegment> segmentsSet = new TreeSet<>(DruidCoordinator.SEGMENT_COMPARATOR_RECENT_FIRST);
    availableSegments.forEach(segmentsSet::add);
    return segmentsSet;
  }