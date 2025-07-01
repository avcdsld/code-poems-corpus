public static ScalingPolicy byDataRate(int targetKBps, int scaleFactor, int minNumSegments) {
        Preconditions.checkArgument(targetKBps > 0, "KBps should be > 0.");
        Preconditions.checkArgument(scaleFactor > 0, "Scale factor should be > 0. Otherwise use fixed scaling policy.");
        Preconditions.checkArgument(minNumSegments > 0, "Minimum number of segments should be > 0.");
        return new ScalingPolicy(ScaleType.BY_RATE_IN_KBYTES_PER_SEC, targetKBps, scaleFactor, minNumSegments);
    }