protected synchronized long seekUnusedZero(Long bucketId, Aggressiveness aggressiveness) {
        AtomicLong freeSpace = new AtomicLong(0);

        int totalElements = (int) memoryHandler.getAllocatedHostObjects(bucketId);

        // these 2 variables will contain jvm-wise memory access frequencies
        float shortAverage = zeroShort.getAverage();
        float longAverage = zeroLong.getAverage();

        // threshold is calculated based on agressiveness specified via configuration
        float shortThreshold = shortAverage / (Aggressiveness.values().length - aggressiveness.ordinal());
        float longThreshold = longAverage / (Aggressiveness.values().length - aggressiveness.ordinal());

        // simple counter for dereferenced objects
        AtomicInteger elementsDropped = new AtomicInteger(0);
        AtomicInteger elementsSurvived = new AtomicInteger(0);

        for (Long object : memoryHandler.getHostTrackingPoints(bucketId)) {
            AllocationPoint point = getAllocationPoint(object);

            // point can be null, if memory was promoted to device and was deleted there
            if (point == null)
                continue;

            if (point.getAllocationStatus() == AllocationStatus.HOST) {
                //point.getAccessState().isToeAvailable()
                //point.getAccessState().requestToe();

                /*
                    Check if memory points to non-existant buffer, using externals.
                    If externals don't have specified buffer - delete reference.
                 */
                if (point.getBuffer() == null) {
                    purgeZeroObject(bucketId, object, point, false);
                    freeSpace.addAndGet(AllocationUtils.getRequiredMemory(point.getShape()));

                    elementsDropped.incrementAndGet();
                    continue;
                } else {
                    elementsSurvived.incrementAndGet();
                }

                //point.getAccessState().releaseToe();
            } else {
                //  log.warn("SKIPPING :(");
            }
        }



        //log.debug("Short average: ["+shortAverage+"], Long average: [" + longAverage + "]");
        //log.debug("Aggressiveness: ["+ aggressiveness+"]; Short threshold: ["+shortThreshold+"]; Long threshold: [" + longThreshold + "]");
        log.debug("Zero {} elements checked: [{}], deleted: {}, survived: {}", bucketId, totalElements,
                        elementsDropped.get(), elementsSurvived.get());

        return freeSpace.get();
    }