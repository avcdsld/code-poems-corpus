public static List<JsonNode> getAppModelReferencedProcessModels(JsonNode appModelJson) {
    List<JsonNode> result = new ArrayList<JsonNode>();
    if (appModelJson.has("models")) {
      ArrayNode modelsArrayNode = (ArrayNode) appModelJson.get("models");
      Iterator<JsonNode> modelArrayIterator = modelsArrayNode.iterator();
      while (modelArrayIterator.hasNext()) {
        result.add(modelArrayIterator.next());
      }
    }
    return result;
  }