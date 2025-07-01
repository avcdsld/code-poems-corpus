public static List<String> getApplicationProfiles(final Environment environment) {
        return Arrays.stream(environment.getActiveProfiles()).collect(Collectors.toList());
    }