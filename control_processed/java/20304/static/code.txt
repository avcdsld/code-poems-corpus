private static String canonicalize(final SortedSet<QueryParameter> sortedParameters) {
		if (sortedParameters == null || sortedParameters.isEmpty()) {
			return "";
		}

		final StringBuilder sb = new StringBuilder(100);
		for (QueryParameter parameter : sortedParameters) {
			final String name = parameter.getName().toLowerCase();
			// Ignore irrelevant parameters
			if (IRRELEVANT_PARAMETERS.contains(name) || name.startsWith("utm_")) {
				continue;
			}
			if (sb.length() > 0) {
				sb.append('&');
			}
			sb.append(parameter.getName());
			if (!parameter.getValue().isEmpty()) {
				sb.append('=');
				sb.append(parameter.getValue());
			}
		}
		return sb.toString();
	}