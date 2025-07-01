private static void formatNames(Iterable<List<String>> names) {
    if (names != null) {
      for (List<String> list : names) {
        String name = list.get(0);
        String[] components = new String[5];
        int start = 0;
        int end;
        int componentIndex = 0;
        while (componentIndex < components.length - 1 && (end = name.indexOf(';', start)) >= 0) {
          components[componentIndex] = name.substring(start, end);
          componentIndex++;
          start = end + 1;
        }
        components[componentIndex] = name.substring(start);
        StringBuilder newName = new StringBuilder(100);
        maybeAppendComponent(components, 3, newName);
        maybeAppendComponent(components, 1, newName);
        maybeAppendComponent(components, 2, newName);
        maybeAppendComponent(components, 0, newName);
        maybeAppendComponent(components, 4, newName);
        list.set(0, newName.toString().trim());
      }
    }
  }