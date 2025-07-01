public static boolean verifyRecordMatchesInput(List<Long> segmentsToSeal, List<Map.Entry<Double, Double>> newRanges,
                                                   boolean isManualScale, EpochTransitionRecord record) {
        // verify that supplied new range matches new range in the record
        boolean newRangeMatch = newRanges.stream().allMatch(x ->
                record.getNewSegmentsWithRange().values().stream()
                        .anyMatch(y -> y.getKey().equals(x.getKey())
                                && y.getValue().equals(x.getValue())));

        if (newRangeMatch) {
            final Set<Integer> segmentNumbersToSeal = isManualScale ? 
                    segmentsToSeal.stream().map(StreamSegmentNameUtils::getSegmentNumber).collect(Collectors.toSet()) :
                    null;
            return segmentsToSeal.stream().allMatch(segmentId -> {
                if (isManualScale) {
                    // compare segmentNumbers
                    return segmentNumbersToSeal.contains(StreamSegmentNameUtils.getSegmentNumber(segmentId));
                } else {
                    // compare segmentIds
                    return record.getSegmentsToSeal().contains(segmentId);
                }
            });
        }
        return false;
    }