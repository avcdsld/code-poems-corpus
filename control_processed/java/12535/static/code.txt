public final T fromJsonTree(JsonElement jsonTree) {
    try {
      JsonReader jsonReader = new JsonTreeReader(jsonTree);
      return read(jsonReader);
    } catch (IOException e) {
      throw new JsonIOException(e);
    }
  }