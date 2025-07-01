private List<String> splitToList(String input)
  {
    Preconditions.checkNotNull(input);

    Iterator<String> iterator = splitter.split(input).iterator();
    List<String> result = new ArrayList<String>();

    while (iterator.hasNext()) {
      result.add(iterator.next());
    }

    return Collections.unmodifiableList(result);
  }