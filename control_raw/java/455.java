public JSONArray getJSONArray(String name) throws JSONException {
		Object object = get(name);
		if (object instanceof JSONArray) {
			return (JSONArray) object;
		}
		else {
			throw JSON.typeMismatch(name, object, "JSONArray");
		}
	}