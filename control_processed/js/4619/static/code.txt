function closeRangeGap(c) {
            // Close the current range
            if (currentRange) {
                currentRange.includesLastSegment = lastMatchIndex >= lastSegmentStart;
                if (currentRange.matched && currentRange.includesLastSegment) {
                    if (DEBUG_SCORES) {
                        scoreDebug.lastSegment += lastSegmentScore * LAST_SEGMENT_BOOST;
                    }
                    score += lastSegmentScore * LAST_SEGMENT_BOOST;
                }

                if (currentRange.matched && !currentRangeStartedOnSpecial) {
                    if (DEBUG_SCORES) {
                        scoreDebug.notStartingOnSpecial -= NOT_STARTING_ON_SPECIAL_PENALTY;
                    }
                    score -= NOT_STARTING_ON_SPECIAL_PENALTY;
                }
                ranges.push(currentRange);
            }

            // If there was space between the new range and the last,
            // add a new unmatched range before the new range can be added.
            if (lastMatchIndex + 1 < c) {
                ranges.push({
                    text: str.substring(lastMatchIndex + 1, c),
                    matched: false,
                    includesLastSegment: c > lastSegmentStart
                });
            }
            currentRange = null;
            lastSegmentScore = 0;
        }