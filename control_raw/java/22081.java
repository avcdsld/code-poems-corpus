@Override
    public CommandLineParser addOption(String name, String description) {
        int length = name.length();
        if (length > longestOptionNameLength) {
            longestOptionNameLength = length;
        }
        declaredOptions.put(name, new Option(name, description));
        return this;
    }