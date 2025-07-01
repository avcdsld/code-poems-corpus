@SuppressWarnings("unused")
    public static List<String> internListOf(Object... objects) {
        if (objects == null || objects.length == 0) {
            return Collections.emptyList();
        }
        List<String> strings = new ArrayList<>(objects.length);
        for (Object object : objects) {
            strings.add(object.toString().intern());
        }
        return Collections.unmodifiableList(strings);
    }