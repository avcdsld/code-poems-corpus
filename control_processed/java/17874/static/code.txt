public TimingStatistics add(TimingStatistics timingStatistics) {
        return TimingStatistics.builder()
                .ndarrayCreationTimeNanos(ndarrayCreationTimeNanos + timingStatistics.ndarrayCreationTimeNanos)
                .bandwidthNanosHostToDevice(bandwidthNanosHostToDevice + timingStatistics.bandwidthNanosHostToDevice)
                .diskReadingTimeNanos(diskReadingTimeNanos + timingStatistics.diskReadingTimeNanos)
                .bandwidthDeviceToHost(bandwidthDeviceToHost + timingStatistics.bandwidthDeviceToHost)
                .build();
    }