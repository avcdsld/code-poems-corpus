public static Response failure(
      SessionId sessionId, Throwable reason, Optional<String> screenshot) {
    Response response = new Response();
    response.setSessionId(sessionId != null ? sessionId.toString() : null);
    response.setStatus(ERROR_CODES.toStatusCode(reason));
    response.setState(ERROR_CODES.toState(response.getStatus()));

    if (reason != null) {
      Json json = new Json();
      String raw = json.toJson(reason);
      Map<String, Object> value = json.toType(raw, MAP_TYPE);
      screenshot.ifPresent(screen -> value.put("screen", screen));
      response.setValue(value);
    }
    return response;
  }