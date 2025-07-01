public static DelimitedStringParser parser(String pairDelimiter, String keyValueDelimiter) {
        Exceptions.checkNotNullOrEmpty(pairDelimiter, "pairDelimiter");
        Exceptions.checkNotNullOrEmpty(keyValueDelimiter, "keyValueDelimiter");
        Preconditions.checkArgument(!pairDelimiter.equals(keyValueDelimiter),
                "pairDelimiter (%s) cannot be the same as keyValueDelimiter (%s)", pairDelimiter, keyValueDelimiter);
        return new DelimitedStringParser(pairDelimiter, keyValueDelimiter);
    }