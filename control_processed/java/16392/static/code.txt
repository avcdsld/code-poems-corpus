public static void insertStopRegexes(String key, String... regexes) {
        StopRecognition fr = get(key);
        fr.insertStopRegexes(regexes);
    }