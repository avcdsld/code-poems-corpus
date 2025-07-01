public static JSONArray toJSONArray(JSONArray names, JSONTokener x) throws JSONException {
    if (names == null || names.length() == 0) {
      return null;
    }
    JSONArray ja = new JSONArray();
    for (;;) {
      JSONObject jo = rowToJSONObject(names, x);
      if (jo == null) {
        break;
      }
      ja.put(jo);
    }
    if (ja.length() == 0) {
      return null;
    }
    return ja;
  }