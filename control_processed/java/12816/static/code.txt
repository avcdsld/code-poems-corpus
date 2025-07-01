public static JSONObject toJSONObject(XMLTokener x) throws JSONException {
    return (JSONObject) parse(x, false, null);
  }