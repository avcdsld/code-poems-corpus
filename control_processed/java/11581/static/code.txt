private static JSONObject toJSONObject(@Nonnull ResourceBundle bundle) {
        JSONObject json = new JSONObject();
        for (String key : bundle.keySet()) {
            json.put(key, bundle.getString(key));
        }
        return json;
    }