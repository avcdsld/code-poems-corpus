public double getDouble(String name) throws JSONException {
		Object object = get(name);
		Double result = JSON.toDouble(object);
		if (result == null) {
			throw JSON.typeMismatch(name, object, "double");
		}
		return result;
	}