@Synchronized
    Set<Segment> getSegments(String reader) {
        Map<Segment, Long> segments = assignedSegments.get(reader);
        if (segments == null) {
            return null;
        }
        return new HashSet<>(segments.keySet());
    }