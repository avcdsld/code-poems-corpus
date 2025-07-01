public static long parseTimestampWithoutTimeZone(String value)
    {
        LocalDateTime localDateTime = TIMESTAMP_WITH_OR_WITHOUT_TIME_ZONE_FORMATTER.parseLocalDateTime(value);
        try {
            return (long) getLocalMillis.invokeExact(localDateTime);
        }
        catch (Throwable e) {
            throw new RuntimeException(e);
        }
    }